from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text

from Bot.keyboard import start_kb


async def start_(message: types.Message):
    await message.bot.send_message(message.from_user.id,"Привет! Я заполняю заявки по указанным Вами данным. Чтобы "
                                                        "просмотреть список компанд нажмите /help", reply_markup=start_kb())


async def help_(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Создать заявку (НК) - /create_contract"
                                                         "\nИзменить старую заявку (ИК) - /update_contract"
                                                         "\nУдалить старую заявку (УК) - /delete_contract"
                                                         "\nУдалить все старые заявки (УдалитьВсе)- /delete_all")


def register_contract_start(dp: Dispatcher):
    dp.register_message_handler(start_, commands=['start'])
    dp.register_message_handler(help_, commands=['help'])
    dp.register_message_handler(help_, Text(equals="Помощь", ignore_case=True))
