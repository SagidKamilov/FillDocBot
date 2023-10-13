"""
Общая клавиатура. Создает список файлов, основанных на папке Contracts/docx/...
"""

from typing import List, Dict

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from file_operations import FindFiles_ShortNameFile


def general_kb(list_doc: List[Dict[str, str]]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    for elem_list in list_doc:
        name_file = elem_list.get(FindFiles_ShortNameFile)
        data_file = elem_list.get(FindFiles_ShortNameFile)
        kb.row(InlineKeyboardButton(text=name_file, callback_data=data_file))
    kb.row(InlineKeyboardButton(text="Отмена", callback_data="cancel_del"))
    return kb
