import asyncio
from aiogram.filters import Command, CommandObject, StateFilter
from aiogram import F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

router = Router()

class QuizQuestions(StatesGroup):
    qq1 = State()
    qq2 = State()
    qq3 = State()
    qq4 = State()
    finish = State()


@router.callback_query(F.data == "start_quiz")
async def starting(callback: types.CallbackQuery):#, state: FSMContext):
    await callback.message.answer('Начинаем!')

    # await state.set_state(QuizQuestions.fgtd.state)

    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='Далее',
            callback_data='r1'
        )
    )
    await callback.message.answer('Викторина состоит из нескольких вопросов, на каждый из них несколько вариантов ответов\nТолько отвечай честно!\nВ конце викторины мы подведём итоги и определим твоё тотемное животное, а таккже ты сможешь больше узнать о программе защиты животных!', reply_markup=builder.as_markup())

    
@router.message(F.data == 'r1')
async def qu1(message: Message):#, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="A",
            callback_data="A"),
        types.InlineKeyboardButton(
            text='B',
            callback_data="B"),
        types.InlineKeyboardButton(
            text='C',
            callback_data="C"),
        types.InlineKeyboardButton(
            text='D',
            callback_data="D"),
        )
    
    await message.answer('Вопрос 1', reply_markup=builder.as_markup())

    # await state.set_state(Quizz.qq2.state)

@router.callback_query(F.data == "A")
async def a1(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(a1='A')

@router.callback_query(F.data == "B")
async def a1(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(a1='B')

@router.callback_query(F.data == "C")
async def a1(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(a1='C')

@router.callback_query(F.data == "D")
async def a1(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(a1='D')


# @router.message(Quizz.qq2)
# async def qu2(message: Message, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(
#         types.InlineKeyboardButton(
#             text="A",
#             callback_data="A"),
#         types.InlineKeyboardButton(
#             text='B',
#             callback_data="B"),
#         types.InlineKeyboardButton(
#             text='C',
#             callback_data="C"),
#         types.InlineKeyboardButton(
#             text='D',
#             callback_data="D"),
#         )
    
#     await message.answer('Вопрос 2', reply_markup=builder.as_markup())

#     await state.set_state(Quizz.qq3.state)

# @router.callback_query(F.data == "A")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a2='A')

# @router.callback_query(F.data == "B")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a2='B')

# @router.callback_query(F.data == "C")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a2='C')

# @router.callback_query(F.data == "D")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a2='D')


# @router.message(Quizz.qq3)
# async def qu3(message: Message, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(
#         types.InlineKeyboardButton(
#             text="A",
#             callback_data="A"),
#         types.InlineKeyboardButton(
#             text='B',
#             callback_data="B"),
#         types.InlineKeyboardButton(
#             text='C',
#             callback_data="C"),
#         types.InlineKeyboardButton(
#             text='D',
#             callback_data="D"),
#         )
    
#     await message.answer('Вопрос 3', reply_markup=builder.as_markup())

#     await state.set_state(Quizz.qq4.state)

# @router.callback_query(F.data == "A")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a3='A')

# @router.callback_query(F.data == "B")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a3='B')

# @router.callback_query(F.data == "C")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a3='C')

# @router.callback_query(F.data == "D")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a3='D')
    

# @router.message(Quizz.qq4)
# async def qu4(message: Message, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(
#         types.InlineKeyboardButton(
#             text="A",
#             callback_data="A"),
#         types.InlineKeyboardButton(
#             text='B',
#             callback_data="B"),
#         types.InlineKeyboardButton(
#             text='C',
#             callback_data="C"),
#         types.InlineKeyboardButton(
#             text='D',
#             callback_data="D"),
#         )
#     await message.answer('Вопрос 4', reply_markup=builder.as_markup())

#     await state.set_state(Quizz.finish.state)

# @router.callback_query(F.data == "A")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a4='A')

# @router.callback_query(F.data == "B")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a4='B')

# @router.callback_query(F.data == "C")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a4='C')

# @router.callback_query(F.data == "D")
# async def a1(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(a4='D')

# @router.message(Quizz.finish)
# async def result(message: Message, state: FSMContext):
#     data = await state.get_data()
#     ans = []
#     for i in range(1, 5):
#         ans.append(data[f"a{i}"])
#     await message.answer(f'Вот твои варианты ответа:{ans}. Остальное будет потом')
