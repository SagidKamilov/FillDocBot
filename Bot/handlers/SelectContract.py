from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import general_kb
# Вызов функций, производящий операции над файлами
from file_operations import find_files
# Вызов констант
from file_operations import path_to_doc, FindFiles_ShortNameFile, FindFiles_NameFile


class SelectContract(StatesGroup):
    step1 = State()


async def select_contract_step1(message: types.Message):
    list_of_doc: list | str = find_files()
    if not list_of_doc:
        text = "Файлы не обнаружены."
        await message.bot.send_message(message.from_user.id, text=text)
    else:
        text = "Выберите договор, который хотите получить:"
        await message.bot.send_message(message.from_user.id, text=text, reply_markup=general_kb(list_of_doc))
        await SelectContract.step1.set()


async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    text = "Выбор отменен!"
    await callback.bot.send_message(callback.from_user.id, text=text)


async def select_contract_step2(callback: types.CallbackQuery, state: FSMContext):
    list_of_doc: list | str = find_files()
    for elem in list_of_doc:
        if elem.get(FindFiles_ShortNameFile) == callback.data:
            path_to_file = path_to_doc + elem.get(FindFiles_NameFile)
            with open(file=path_to_file, mode="rb") as file:
                await callback.bot.send_document(callback.from_user.id, document=file)
            file.close()
        #     break
        # else:
        #     continue
    await state.finish()


def register_handler_select_contract(dp: Dispatcher):
    dp.register_message_handler(select_contract_step1, commands=["select_contract"], state=None)
    dp.register_callback_query_handler(cancel, Text(equals="cancel"), state='*')
    dp.register_message_handler(select_contract_step1, Text(equals="Выбрать контракт"), state=None)
    dp.register_callback_query_handler(select_contract_step2,
                                       lambda message: message.data in [elem.get(FindFiles_ShortNameFile)
                                                                        for elem in
                                                                        find_files()], state=SelectContract.step1)
