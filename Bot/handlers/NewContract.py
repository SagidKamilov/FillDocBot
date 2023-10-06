from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import choice_template
from Bot.utils import check_date

class NewContract(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()


async def start_(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Вы выбрали \"Новый контракт\". Выберите Шаблон:",
                                   reply_markup=choice_template())
    await NewContract.step1.set()


async def stop_(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data.clear()
    await state.finish()
    await message.bot.send_message(message.from_user.id, "Создание документа отменено.")


async def step1(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["template"] = callback.data
    await callback.bot.send_message(callback.from_user.id, "Введите рейс: Точка1 Точка2")


async def step2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["flight_info"] = message.text.replace(' ', '-')
    await message.bot.send_message(message.from_user.id, "Введите дату создания договора: дд.мм.гггг")
    await NewContract.next()


async def step3(message: types.Message, state: FSMContext):
    if check_date(message.text):
        async with state.proxy() as data:
            data["date"] = message.text
        await NewContract.next()
        await message.bot.send_message(message.from_user.id, "")
    else:
        await message.bot.send_message(message.from_user.id, "Неправильный формат даты!")



def register_handler_new_contract(dp: Dispatcher):
    dp.register_message_handler(start_, commands="new_contract")
    dp.register_message_handler(start_, Text(equals="нк", ignore_case=True))
    dp.register_callback_query_handler(stop_, Text(equals="stop"))
    dp.register_message_handler(step1, )

