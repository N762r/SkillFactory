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

router = Router()

@router.message(Command('categorysearchrandom'))
async def cmd_search(message: Message, command: CommandObject, state: FSMContext):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return

    await state.set_data({'num_recipes': int(command.args[0])})

    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list') as resp:
            categories_data = await resp.json()
            categories = [cat['strCategory'] for cat in categories_data['meals']]
    
    kb_ct = [
        []
    ]
    for category in categories:
        kb_ct.append(types.KeyboardButton(text=f'{category}'))
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_ct,
        resize_keyboard=True,
    )

    await message.reply("Выберите категорию рецепта:", reply_markup=keyboard)