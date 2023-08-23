from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from django.conf import settings
from django.core.management import BaseCommand
from telegram_bot.config import *
from telegram_bot.handlers.base import register_base
from telegram_bot.handlers.consultant import register_consultant


class Command(BaseCommand):  # noqa
    dp.middleware.setup(LoggingMiddleware())

    register_base(dp)
    register_consultant(dp)

    async def shutdown(dispatcher: Dispatcher):
        await dispatcher.storage.close()
        await dispatcher.storage.wait_closed()

    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
