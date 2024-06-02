import asyncio
from random import choices
from aiogram.filters import Command, CommandObject, StateFilter
from aiogram import F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

router = Router()

class Quizz(StatesGroup):
    question = State()

@router.callback_query(F.data == "start_quiz")
async def starting(callback: types.CallbackQuery):
    await callback.message.answer('Начинаем!')

    await callback.message.answer('Викторина состоит из нескольких вопросов, на каждый из них несколько вариантов ответов\nТолько отвечай честно!\nВ конце викторины мы подведём итоги и определим твоё тотемное животное, а таккже ты сможешь больше узнать о программе защиты животных!')