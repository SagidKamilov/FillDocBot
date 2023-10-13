"""
Общая клавиатура. Создает список файлов, основанных на папке Contracts/docx/...
"""

from typing import List, Dict

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from file_operations import find_files_name_file


def general_kb(list_doc):
    kb = InlineKeyboardMarkup()
    for elem_list in list_doc:
        name_file = elem_list.get(find_files_name_file)
        data_file = elem_list.get(find_files_name_file)
        print(data_file)
        kb.row(InlineKeyboardButton(text=name_file, callback_data=data_file))
    kb.row(InlineKeyboardButton(text="Отмена", callback_data="cancel_del"))
    return kb