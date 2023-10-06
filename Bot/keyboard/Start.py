from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup()
    but1 = KeyboardButton("НК")
    but2 = KeyboardButton("Помощь")
    return kb.row(but1, but2)
