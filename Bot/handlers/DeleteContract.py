from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import general_kb
# Вызов функций, производящий операции над файлами
from file_operations import find_files, delete_file, delete_files
# Вызов констант
from file_operations import path_to_doc


class DeleteContract(StatesGroup):
    step1 = State()


async def delete_contract_step1(message: types.Message):
    list_of_doc: list = find_files()
    await message.bot.send_message(message.from_user.id, "Выберите договор, который надо удалить:",
                                   reply_markup=general_kb(list_of_doc))
    await DeleteContract.step1.set()


async def delete_contract_step2(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "cancel_del":
        await callback.bot.edit_message_text(text="Удаление файлов остановлено!")
        await state.finish()
    else:
        list_of_doc: list = find_files()
        result: str = delete_file(file_name=callback.data[:-1]) + " Хотите еще удалить что-нибудь?"
        await callback.bot.edit_message_text(text=result, reply_markup= general_kb(list_of_doc))
        await DeleteContract.previous()


async def delete_all(message: types.Message):
    result = delete_files(path_to_dir=path_to_doc)
    await message.bot.send_message(message.from_user.id, text=result)


def register_handler_delete_contract(dp: Dispatcher):
    dp.register_message_handler(delete_contract_step1, commands=["delete_contract"], state=None)
    dp.register_message_handler(delete_contract_step1, Text(equals="Удалить файл"), state=None)
    dp.register_callback_query_handler(delete_contract_step2,
                                       lambda message:  message.data == "Заявка" or message.data == "cancel_del",
                                       state=DeleteContract.step1)
    dp.register_message_handler(delete_all, commands=["delete_all"])
    dp.register_message_handler(delete_all, Text(equals="Удалить все файлы"))
