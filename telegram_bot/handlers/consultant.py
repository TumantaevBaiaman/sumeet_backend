from functools import partial

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    ReplyKeyboardMarkup,
)
from django.core.paginator import Paginator

from consultation.models import Question, Consultant, Answer
from telegram_bot.config import bot

from telegram_bot.handlers.buttons import (
    consultant_key,
    button_page_next,
    button_page_previous,
)


class FSMAnswer(StatesGroup):
    question_id = State()
    answer = State()
    page = 0


async def cm_start_answer(message: types.Message, state: FSMContext):
    consultant = Consultant.objects.get(telegram_id=message.from_user.id)
    user_questions = Question.objects.filter(consultant=consultant, answer__isnull=True).order_by("created")
    questions_per_page = 5

    async with state.proxy() as data:
        try:
            data["page"]
        except KeyError:
            data["page"] = 1

    async with state.proxy() as data:
        page_number = data["page"]

    paginator = Paginator(user_questions, questions_per_page)

    page = paginator.get_page(page_number)

    for question in page:
        buttons = [InlineKeyboardButton(text="Ответить", callback_data=f"question:{question.id}")]
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)

        await bot.send_message(
            message.from_user.id,
            text=f"""
    Пользователь: 
    Никнейм: {question.user.username}
    Телефон: {question.user.phone}
    Имя: {question.user.first_name}
    Фамилия: {question.user.last_name}

    Вопрос:
    {question.topic}: {question.text}

    Результат:
    {question.result}
            """,
            reply_markup=keyboard,
        )

    page_key = ReplyKeyboardMarkup(resize_keyboard=True)
    if page.has_previous():
        page_key.add(button_page_previous)
    if page.has_next():
        page_key.add(button_page_next)

    await bot.send_message(message.from_user.id, text="Выберите действие:", reply_markup=page_key)


async def next_pages(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["page"] += 1
    await cm_start_answer(msg, state)


async def prev_pages(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["page"] -= 1
    await cm_start_answer(msg, state)


async def question_selected(callback_query: CallbackQuery, state: FSMContext):
    question_id = callback_query.data.split(":")[1]
    await state.update_data(question_id=question_id)

    await FSMAnswer.answer.set()

    await bot.send_message(callback_query.from_user.id, "Пишите ответ для этого вопроса:")


async def answer_received(msg: types.Message, state: FSMContext):
    answer_text = msg.text
    data = await state.get_data()

    answer = Answer.objects.create(question_id=data.get("question_id"), answer=answer_text)
    answer.save()

    await bot.send_message(
        msg.from_user.id,
        f"Ответ сохранён.\nAnswer ID: {answer.id}",
        reply_markup=consultant_key,
    )
    await state.finish()


def register_consultant(dp: Dispatcher):
    dp.register_message_handler(
        partial(cm_start_answer, state=FSMAnswer),
        Text(equals="❔Вопросы", ignore_case=True),
    )
    dp.register_message_handler(
        partial(next_pages, state=FSMAnswer.page),
        Text(equals="Следующая", ignore_case=True),
    )
    dp.register_message_handler(
        partial(prev_pages, state=FSMAnswer.page),
        Text(equals="Предыдущая", ignore_case=True),
    )
    dp.register_callback_query_handler(question_selected)
    dp.register_message_handler(answer_received, state=FSMAnswer)
