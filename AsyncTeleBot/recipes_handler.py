import aiohttp
import json
import random
from random import choices
from aiogram.filters import Command, CommandObject, StateFilter
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
    getting_recipes = State()


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

    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={chosen_category}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                await message.reply("Произошла ошибка при получении данных.")
                return

            data = await response.json()

            if 'meals' not in data:
                await message.reply("По выбранной категории нет рецептов.")
                return

            recipes = []
            for meal in data['meals']:
                rec = meal['strMeal']
                r = translator.translate(f'{rec}', dest='ru')
                recipes.append(r.text)

            data = await state.get_data()
            num_recipes = data.get("num_recipes")

            random_recipes = random.choices(recipes, k=num_recipes)
            random_recipes = ', '.join(random_recipes)
            kb = [[types.KeyboardButton(text="Покажи рецепты"),],]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,)

            await message.answer(f'Как Вам такие варианты: {random_recipes}', reply_markup=keyboard)
