import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from token_data import TOKEN
from aiogram import F
from aiogram.utils.formatting import (
   Bold, as_list, as_marked_section
)
from recipes_handler import router
dp = Dispatcher()
dp.include_router(router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
      [
          types.KeyboardButton(text="Команды"),
          types.KeyboardButton(text="Описание"),
      ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!", reply_markup=keyboard)

@dp.message(F.text.lower() == "команды")
async def commands(message: types.Message) -> None:
    await message.answer("/categorysearchrandom - Случайные рецепты из выбранной категории")

@dp.message(F.text.lower() == "описание")
async def description(message: types.Message) -> None:
    await message.answer("Это кулинарный бот, предоставляющий информацию о рецептах ингредиентах и категориях блюд")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())