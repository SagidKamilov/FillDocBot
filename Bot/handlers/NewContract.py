from typing import Dict

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import choice_template, cancel_enter
from utils import check_date
from contract_fill import fill_doc
from file_operations import find_files
from file_operations import path_to_doc


class NewContract(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()
    step6 = State()
    step7 = State()
    step8 = State()
    step9 = State()
    step10 = State()
    step11 = State()
    step12 = State()
    step13 = State()
    step14 = State()
    step15 = State()
    step16 = State()
    step17 = State()
    step18 = State()
    step19 = State()
    step20 = State()
    step21 = State()
    step22 = State()
    step23 = State()
    step24 = State()
    step25 = State()
    step26 = State()
    step27 = State()
    step28 = State()
    step29 = State()
    step30 = State()
    step31 = State()


def get_index_message(data, message):
    messages = data.get("messages")
    n = messages.index(message)
    return n


async def start_(message: types.Message, state: FSMContext):
    await NewContract.step1.set()
    text = "Вы выбрали \"Новый контракт\" (Если не знаете, что выбрать, то поставьте точку). Выберите Шаблон:"
    await message.bot.send_message(message.from_user.id, text=text, reply_markup=choice_template())
    async with state.proxy() as data:
        data['n'] = -1
        data["messages"] = []


async def stop_(message: types.Message, state: FSMContext):
    text = "Создание документа отменено."
    async with state.proxy() as data:
        data.clear()
    await state.finish()
    await message.bot.send_message(message.from_user.id, text=text)


async def back(callback: types.CallbackQuery, state: FSMContext):
    await NewContract.previous()
    async with state.proxy() as data:
        # meta_message_id = list(data.keys())[-1]
        # back_meta_message_id = "message" + str(data[meta_message_id].get("id") - 1)
        # text = data.get(back_meta_message_id).get("text")
        # print(meta_message_id[-1])
        n = data.get('n')
        data['n'] = n - 1
        text = data.get("messages")[data.get('n')]
    await callback.bot.send_message(callback.from_user.id, text, reply_markup=cancel_enter())


async def step1(callback: types.CallbackQuery, state: FSMContext):
    text = "Введите дату создания договора: дд.мм.гггг"
    async with state.proxy() as data:
        data["template"] = callback.data
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await callback.bot.send_message(callback.from_user.id, text, reply_markup=cancel_enter())
    await NewContract.next()


async def step2(message: types.Message, state: FSMContext):
    if check_date(message.text):
        text = "Адрес погрузки:"
        async with state.proxy() as data:
            data["date"] = message.text
            data["messages"].append(text)
            data['n'] = get_index_message(data, text)

        await NewContract.next()
        await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())
    else:
        text = "Неправильный формат даты!"
        await message.bot.send_message(message.from_user.id, text=text, reply_markup=cancel_enter())


async def step3(message: types.Message, state: FSMContext):
    text = "Введите дату и время погрузки:"
    async with state.proxy() as data:
        data["from_address"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())
    await NewContract.next()


async def step4(message: types.Message, state: FSMContext):
    text = "Контактное лицо, отвечающее за погрузку:"
    async with state.proxy() as data:
        data["from_date"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step5(message: types.Message, state: FSMContext):
    text = "Номер контактного лица, отвечающего за погрузку:"
    async with state.proxy() as data:
        data["contact_person_from"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step6(message: types.Message, state: FSMContext):
    text = "Введите адрес разгрузки: "
    async with state.proxy() as data:
        data["contact_person_from_phone"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step7(message: types.Message, state: FSMContext):
    text = "Введите дату и время разгрузки"
    async with state.proxy() as data:
        data["to_address"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step8(message: types.Message, state: FSMContext):
    text = "Контактное лицо, отвечающее за погрузку:"
    async with state.proxy() as data:
        data["to_date"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step9(message: types.Message, state: FSMContext):
    text = "Номер контактного лица, отвечающего за погрузку:"
    async with state.proxy() as data:
        data["contact_person_to"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step10(message: types.Message, state: FSMContext):
    text = "Требуемый вид подвижного состава"
    async with state.proxy() as data:
        data["contact_person_to_phone"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step11(message: types.Message, state: FSMContext):
    text = "Наименование груза, объем и рамзмеры:"
    async with state.proxy() as data:
        data["type_machine"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step12(message: types.Message, state: FSMContext):
    text = "Вид загрузки:"
    async with state.proxy() as data:
        data["name_cargo"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step13(message: types.Message, state: FSMContext):
    text = "Вид выгрузки:"
    async with state.proxy() as data:
        data["type_loading"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step14(message: types.Message, state: FSMContext):
    text = "Деньги для ЗАКАЗЧИКА:"
    async with state.proxy() as data:
        data["type_unloading"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step15(message: types.Message, state: FSMContext):
    text = "Деньги для ПЕРЕВОЗЧИКА:"
    async with state.proxy() as data:
        data["price_customer"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step16(message: types.Message, state: FSMContext):
    text = "Марка автомобиля:"
    async with state.proxy() as data:
        data["price_driver"] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step17(message: types.Message, state: FSMContext):
    text = "Гос. номер:"
    async with state.proxy() as data:
        data['car_model'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step18(message: types.Message, state: FSMContext):
    text = "Марка П./П.:"
    async with state.proxy() as data:
        data['car_number'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step19(message: types.Message, state: FSMContext):
    text = "Гос. номер П./П.:"
    async with state.proxy() as data:
        data['trailer_model'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step20(message: types.Message, state: FSMContext):
    text = "ФИО водителя:"
    async with state.proxy() as data:
        data['trailer_number'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step21(message: types.Message, state: FSMContext):
    text = "Номер телефона водителя:"
    async with state.proxy() as data:
        data['name_driver'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step22(message: types.Message, state: FSMContext):
    text = "Паспорт водителя:"
    async with state.proxy() as data:
        data['phone_driver'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step23(message: types.Message, state: FSMContext):
    text = "Контакты менеджера (твои):"
    async with state.proxy() as data:
        data['passport_driver'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step24(message: types.Message, state: FSMContext):
    text = "Информация о ЗАКАЗЧИКЕ (ИП/ФИЗ и т.п.):"
    async with state.proxy() as data:
        data['contact_manager'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step25(message: types.Message, state: FSMContext):
    text = "Сокращенное название организации ЗАКАЗЧИКА:"
    async with state.proxy() as data:
        data['info_customer'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step26(message: types.Message, state: FSMContext):
    text = "Полноне название организации ЗАКАЗЧИКА:"
    async with state.proxy() as data:
        data['short_org_name_customer'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step27(message: types.Message, state: FSMContext):
    text = "Информация о ПЕРЕВОЗЧИКЕ (ИП/ФИЗ и т.п.):"
    async with state.proxy() as data:
        data['full_org_name_customer'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step28(message: types.Message, state: FSMContext):
    text = "Сокращенное название организации ПЕРЕВОЗЧИКА:"
    async with state.proxy() as data:
        data['carrier_info'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step29(message: types.Message, state: FSMContext):
    text = "Полное название организации ПЕРЕВОЗЧИКА:"
    async with state.proxy() as data:
        data['short_org_name_carrier'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step30(message: types.Message, state: FSMContext):
    text = "Маршрут (Город1-Города2):"
    async with state.proxy() as data:
        data['full_org_name_carrier'] = message.text
        data["messages"].append(text)
        data['n'] = get_index_message(data, text)

    await NewContract.next()
    await message.bot.send_message(message.from_user.id, text, reply_markup=cancel_enter())


async def step31(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["flight"] = message.text

    await message.bot.send_message(message.from_user.id, text="Данные приняты. Идет обработка...")
    result = fill_doc(info_doc=data)
    for path_to_file in result:
        path_to_file: str = path_to_doc + path_to_file
        with open(file=path_to_file, mode="rb") as file:
            await message.bot.send_document(message.from_user.id, document=file)
        file.close()
    await state.finish()


def register_handler_new_contract(dp: Dispatcher):
    dp.register_message_handler(start_, commands=["new_contract"], state=None)
    dp.register_message_handler(start_, Text(equals="нк", ignore_case=True), state=None)
    dp.register_callback_query_handler(stop_, Text(equals="stop"), state='*')
    dp.register_callback_query_handler(back, Text(equals="back"), state='*')
    dp.register_callback_query_handler(step1, Text(equals=['М', 'Б'], ignore_case=True), state=NewContract.step1)
    dp.register_message_handler(step2, content_types=["text"], state=NewContract.step2)
    dp.register_message_handler(step3, content_types=["text"], state=NewContract.step3)
    dp.register_message_handler(step4, content_types=["text"], state=NewContract.step4)
    dp.register_message_handler(step5, content_types=["text"], state=NewContract.step5)
    dp.register_message_handler(step6, content_types=["text"], state=NewContract.step6)
    dp.register_message_handler(step7, content_types=["text"], state=NewContract.step7)
    dp.register_message_handler(step8, content_types=["text"], state=NewContract.step8)
    dp.register_message_handler(step9, content_types=["text"], state=NewContract.step9)
    dp.register_message_handler(step10, content_types=["text"], state=NewContract.step10)
    dp.register_message_handler(step11, content_types=["text"], state=NewContract.step11)
    dp.register_message_handler(step12, content_types=["text"], state=NewContract.step12)
    dp.register_message_handler(step13, content_types=["text"], state=NewContract.step13)
    dp.register_message_handler(step14, content_types=["text"], state=NewContract.step14)
    dp.register_message_handler(step15, content_types=["text"], state=NewContract.step15)
    dp.register_message_handler(step16, content_types=["text"], state=NewContract.step16)
    dp.register_message_handler(step17, content_types=["text"], state=NewContract.step17)
    dp.register_message_handler(step18, content_types=["text"], state=NewContract.step18)
    dp.register_message_handler(step19, content_types=["text"], state=NewContract.step19)
    dp.register_message_handler(step20, content_types=["text"], state=NewContract.step20)
    dp.register_message_handler(step21, content_types=["text"], state=NewContract.step21)
    dp.register_message_handler(step22, content_types=["text"], state=NewContract.step22)
    dp.register_message_handler(step23, content_types=["text"], state=NewContract.step23)
    dp.register_message_handler(step24, content_types=["text"], state=NewContract.step24)
    dp.register_message_handler(step25, content_types=["text"], state=NewContract.step25)
    dp.register_message_handler(step26, content_types=["text"], state=NewContract.step26)
    dp.register_message_handler(step27, content_types=["text"], state=NewContract.step27)
    dp.register_message_handler(step28, content_types=["text"], state=NewContract.step28)
    dp.register_message_handler(step29, content_types=["text"], state=NewContract.step29)
    dp.register_message_handler(step30, content_types=["text"], state=NewContract.step30)
    dp.register_message_handler(step31, content_types=["text"], state=NewContract.step31)


