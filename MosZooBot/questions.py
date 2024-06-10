from aiogram import F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

class QuiZz(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    finita_la_comedia = State()


@router.callback_query(F.data == 'start_quiz')
async def starting(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='Начинаем!',
            callback_data='run'
        )
    )
    await callback.message.answer('Викторина состоит из нескольких вопросов, на каждый из них несколько вариантов ответов\nТолько отвечай честно!\nВ конце викторины мы подведём итоги и определим твоё тотемное животное, а таккже ты сможешь больше узнать о программе защиты животных!', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.question1)
    

    
@router.callback_query(QuiZz.question1, F.data == 'run')
async def qu1(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='A',
            callback_data='A'),
        types.InlineKeyboardButton(
            text='B',
            callback_data='B'),
        types.InlineKeyboardButton(
            text='C',
            callback_data='C'),
        types.InlineKeyboardButton(
            text='D',
            callback_data='D'),
        )
  
    await callback.message.answer('Вопрос 1', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.question2)



@router.callback_query(QuiZz.question2)
async def qu2(callback: types.CallbackQuery, state: FSMContext):
    a1 = callback.data
    await state.update_data(a1 = a1)

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='A',
            callback_data='A'),
        types.InlineKeyboardButton(
            text='B',
            callback_data='B'),
        types.InlineKeyboardButton(
            text='C',
            callback_data='C'),
        types.InlineKeyboardButton(
            text='D',
            callback_data='D'),
        )
    
    await callback.message.answer('Вопрос 2', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.question3)



@router.callback_query(QuiZz.question3)
async def qu3(callback: types.CallbackQuery, state: FSMContext):
    a2 = callback.data
    await state.update_data(a2 = a2)

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='A',
            callback_data='A'),
        types.InlineKeyboardButton(
            text='B',
            callback_data='B'),
        types.InlineKeyboardButton(
            text='C',
            callback_data='C'),
        types.InlineKeyboardButton(
            text='D',
            callback_data='D'),
        )
    
    await callback.message.answer('Вопрос 3', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.question4)


@router.callback_query(QuiZz.question4)
async def qu4(callback: types.CallbackQuery, state: FSMContext):
    a3 = callback.data
    await state.update_data(a3 = a3)

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='A',
            callback_data='A'),
        types.InlineKeyboardButton(
            text='B',
            callback_data='B'),
        types.InlineKeyboardButton(
            text='C',
            callback_data='C'),
        types.InlineKeyboardButton(
            text='D',
            callback_data='D'),
        )
    
    await callback.message.answer('Вопрос 4', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.question5)



@router.callback_query(QuiZz.question5)
async def qu5(callback: types.CallbackQuery, state: FSMContext):
    a4 = callback.data
    await state.update_data(a4 = a4)

    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text='A',
            callback_data='A'),
        types.InlineKeyboardButton(
            text='B',
            callback_data='B'),
        types.InlineKeyboardButton(
            text='C',
            callback_data='C'),
        types.InlineKeyboardButton(
            text='D',
            callback_data='D'),
        )
    
    await callback.message.answer('Вопрос 5', reply_markup=builder.as_markup())

    await state.set_state(QuiZz.finita_la_comedia)



@router.callback_query(QuiZz.finita_la_comedia)
async def finit(callback: types.CallbackQuery, state: FSMContext):
    a5 = callback.data
    await state.update_data(a5 = a5)

    data = await state.get_data()
    answers = [data.get('a1'), data.get('a2'), data.get('a3'), data.get('a4'), data.get('a5'), ]
    result = max(set(answers), key=answers.count)
    await callback.message.answer(f"{result}")

    await state.clear
