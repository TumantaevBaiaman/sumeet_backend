import json

from aiogram import types
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from telegram_bot.config import dp


@csrf_exempt
async def telegram_webhook(request):
    """
    webhook telegram view
    """
    try:
        data = json.loads(request.body)
        update = types.Update(**data)
        await dp.process_update(update)
        return JsonResponse({"status": "ok"})
    except Exception as e:
        return JsonResponse({"status": "error", "error": str(e)})
