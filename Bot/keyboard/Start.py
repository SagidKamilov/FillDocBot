from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("НК")
    but2 = KeyboardButton("Помощь")
    return kb.row(but1, but2)
