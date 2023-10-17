from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import general_kb
# Вызов функций, производящий операции над файлами
from file_operations import find_files, delete_file, delete_files
# Вызов констант
from file_operations import path_to_doc, FindFiles_ShortNameFile, FindFiles_NameFile


class DeleteContract(StatesGroup):
    step1 = State()


async def delete_contract_step1(message: types.Message):
    list_of_doc: list | str = find_files()
    if not list_of_doc:
        text = "Файлы не обнаружены."
        await message.bot.send_message(message.from_user.id, text=text)
    else:
        text = "Выберите договор, который надо удалить:"
        await message.bot.send_message(message.from_user.id, text=text, reply_markup=general_kb(list_of_doc))
        await DeleteContract.step1.set()


async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    text = "Выбор отменен!"
    await callback.bot.send_message(callback.from_user.id, text=text)


async def delete_contract_step2(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "cancel_del":
        text = "Удаление файлов остановлено!"
        await callback.bot.send_message(callback.from_user.id, text=text)
        await state.finish()
    else:
        list_of_doc: list = find_files()
        result: str
        for elem in list_of_doc:
            if elem.get(FindFiles_ShortNameFile) == callback.data:
                result = delete_file(file_name=elem.get(FindFiles_NameFile))
                await callback.bot.send_message(callback.from_user.id, text=result)
                break
            else:
                continue
        text = "Хотите еще удалить что-нибудь?"
        await callback.bot.send_message(callback.from_user.id, text=text, reply_markup=general_kb(list_of_doc))


async def delete_all(message: types.Message):
    result = delete_files(path_to_dir=path_to_doc)
    await message.bot.send_message(message.from_user.id, text=result)


def register_handler_delete_contract(dp: Dispatcher):
    dp.register_message_handler(delete_contract_step1, commands=["delete_contract"], state=None)
    dp.register_callback_query_handler(cancel, Text(equals="cancel"), state='*')
    dp.register_message_handler(delete_contract_step1, Text(equals="Удалить файл"), state=None)
    dp.register_callback_query_handler(delete_contract_step2,
                                       lambda message: message.data in [elem.get(FindFiles_ShortNameFile)
                                                                        for elem in
                                                                        find_files()],
                                       state=DeleteContract.step1)
    dp.register_message_handler(delete_all, commands=["delete_all"])
    dp.register_message_handler(delete_all, Text(equals="Удалить все файлы"))
