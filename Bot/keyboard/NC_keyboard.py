from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choice_template():
    kb = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text="Баданина", callback_data="Б")
    but2 = InlineKeyboardButton(text="Макова", callback_data="М")
    return kb.row(but1, but2)


# def
