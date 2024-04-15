import aiohttp
import json
import random
import asyncio
from random import choices
from aiogram.filters import Command, CommandObject, StateFilter
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from googletrans import Translator
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()
translator = Translator()

class RecipeSearchStates(StatesGroup):
    category_selection = State()
    finall = State()

@router.message(Command('categorysearchrandom'))
async def cmd_search(message: Message, command: CommandObject, state: FSMContext):
    if not command.args:
        await message.reply("Пожалуйста, укажите число рецептов после команды.")
        return

    try:
        num_recipes = int(command.args[0])
    except ValueError:
        await message.reply("Неверный формат числа рецептов.")
        return

    await state.update_data(num_recipes=num_recipes)

    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list') as resp:
            categories_data = await resp.json()

    keyboard_builder = ReplyKeyboardBuilder()
    for category in categories_data['meals']:
        category_name = category['strCategory']
        keyboard_builder.add(types.KeyboardButton(text = category_name))
    keyboard_builder.adjust(4)

    await message.answer("Выберите категорию:", reply_markup=keyboard_builder.as_markup(resise_keyboard=True))

    await state.set_state(RecipeSearchStates.category_selection.state)


@router.message(RecipeSearchStates.category_selection)
async def handle_category_choice(message: Message, state: FSMContext):
    chosen_category = message.text

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={chosen_category}') as response:
            if response.status != 200:
                await message.reply("Произошла ошибка при получении данных.")
                return

            data = await response.json()

            if 'meals' not in data:
                await message.reply("По выбранной категории нет рецептов.")
                return

            recipes = [meal['strMeal'] for meal in data['meals']]
            id_recipes = [meal['idMeal'] for meal in data['meals']]
            id_dic = {}
            for i in range(len(recipes)):
                id_dic[recipes[i]] = id_recipes[i]

            data = await state.get_data()
            num_recipes = data.get("num_recipes")

            random_recipe = random.choices(recipes, k=num_recipes)
            random_recipe_id = [id_dic.get(f'{recipe}') for recipe in random_recipe]
            await state.update_data(random_recipe_id=random_recipe_id)

            random_recipes = ', '.join(random_recipe)
            random_recipes_translate = translator.translate(f'{random_recipes}', dest='ru')

            kb = [[types.KeyboardButton(text="Покажи рецепты"),],]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)

            await message.answer(f'Как Вам такие варианты: {random_recipes_translate.text}', reply_markup=keyboard)

            await state.set_state(RecipeSearchStates.finall.state)            

@router.message(RecipeSearchStates.finall)
async def recipes_descript_getter(message: Message, state: FSMContext):
    view = message.text

    async def fetch_recipe(recipe_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}') as response:
                data = await response.json()
                return data

    async def process_recipes(recipe_ids):
        tasks = [fetch_recipe(recipe_id) for recipe_id in recipe_ids]
        recips = await asyncio.gather(*tasks)
        return recips

    data = await state.get_data()
    recipe_ids = data.get("random_recipe_id")
    recips = await process_recipes(recipe_ids)
    for recipe in recips:
        name = recipe['meals'][0]['strMeal']
        instruction = recipe['meals'][0]['strInstructions']
        ingredients = []
        for key, value in recipe['meals'][0].items():
            if key.startswith('strIngredient') and value is not None and value.strip() != '':
                ingredient = value.strip()
                ingredients.append(ingredient)
        ingredients = ', '.join(ingredients)
        if view == F.text.lower('покажи рецепты'):
            await message.answer('\n\n'.join([translator.translate(f'{text}', dest='ru').text for text in [name, instruction, ingredients]]))
