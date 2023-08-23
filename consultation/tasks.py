import asyncio

from celery import shared_task

from consultation.models import Question
from telegram_bot.config import bot


async def send_message_async(question):
    expert_chat_id = question.consultant.telegram_id
    await bot.send_message(
        expert_chat_id,
        text=f"""
✅Новый вопрос для вас
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
    )


@shared_task
def process_data(question_id):
    question = Question.objects.get(id=str(question_id))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_async(question=question))
