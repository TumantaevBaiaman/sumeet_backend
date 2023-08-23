from aiogram import types, Dispatcher

from consultation.models import Question
from telegram_bot.config import dp, bot
from telegram_bot.decorators import decorate_auth
from telegram_bot.handlers.buttons import consultant_key


@decorate_auth
async def start(msg: types.Message, user: types.User):
    await bot.send_message(user.id, "Welcome consultant.", reply_markup=consultant_key)


def register_base(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state=None)
