from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_questions = KeyboardButton("❔Вопросы")
consultant_key = ReplyKeyboardMarkup(resize_keyboard=True).add(button_questions)

button_page_next = KeyboardButton("Следующая")
button_page_previous = KeyboardButton("Предыдущая")
