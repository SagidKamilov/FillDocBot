from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("НК")
    but2 = KeyboardButton("Помощь")
    but3 = KeyboardButton("Удалить файл")
    but4 = KeyboardButton("Удалить все файлы")
    return kb.row(but1, but2).row(but3, but4)
