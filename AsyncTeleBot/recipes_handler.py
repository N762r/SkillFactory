import aiohttp
import json

from datetime import datetime

from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.formatting import (
   Bold, as_list, as_marked_section
)
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

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
    #await RecipeSearchStates.CategorySelection.set()
