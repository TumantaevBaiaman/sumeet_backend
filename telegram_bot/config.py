from unittest.mock import Mock
import sys
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from django.conf import settings

print(f"SYS ARGV {sys.argv}")

if ("test" or "pytest") not in sys.argv[0]:
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(LoggingMiddleware())
else:
    bot = Mock()
    dp = Mock()
