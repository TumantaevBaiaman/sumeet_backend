from aiogram import types
from consultation.models import Consultant
from telegram_bot.config import bot
from functools import wraps


def decorate_auth(func):
    """
    auth decorate telegram
    """

    @wraps(func)
    async def wrapper(msg: types.Message):
        try:
            user: types.User = msg.from_user
            auth_user = Consultant.objects.get(telegram_id=user.id)
            if not auth_user:
                await bot.send_message(
                    user.id,
                    "Вы не можете возпользовать этот телеграм бот. Так как вы не являетесь консультатом.",
                )
            else:
                return await func(msg, user)
        except Exception as ex:  # noqa
            return await msg.reply("Произошла ошибка при обработке вашего запроса.")

    return wrapper
