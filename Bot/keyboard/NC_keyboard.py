from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choice_template() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text="Баданина", callback_data='Б')
    but2 = InlineKeyboardButton(text="Макова", callback_data='М')
    return kb.row(but1, but2)


def cancel_enter() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text="Завершить заполнени", callback_data="stop")
    but2 = InlineKeyboardButton(text="Назад", callback_data="back")
    return kb.row(but2).row(but1)
