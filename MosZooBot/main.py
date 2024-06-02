import asyncio 
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from TOKEN import TOKEN
from questions import router
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

dp = Dispatcher()
dp.include_router(router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Поехали!",
            callback_data="start_quiz"),
        types.InlineKeyboardButton(
            text='Погоди',
            callback_data="wait")
        )

    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!\nЯ бот Московского зоопарка!\nЯ расскажу тебе о программе опеки, а чтобы тебе было не скучно, предлагаю сыграть в викторину и определить твоё тотемное животное!\nНачнём?',
                        reply_markup=builder.as_markup())

@dp.callback_query(F.data == "wait")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(   
        types.InlineKeyboardButton(
            text='Наш сайт',
            url='https://moscowzoo.ru/')
        )
    await callback.message.answer('Хорошо, жду\nПока можешь посетить наш сайт', reply_markup=builder.as_markup())

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())