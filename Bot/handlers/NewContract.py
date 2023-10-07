from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from Bot.keyboard import choice_template, cancel_enter
from Bot.utils import check_date


class NewContract(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()


async def start_(message: types.Message):
    await NewContract.step1.set()
    await message.bot.send_message(message.from_user.id, "Вы выбрали \"Новый контракт\". Выберите Шаблон:",
                                   reply_markup=choice_template())


async def stop_(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data.clear()
    await state.finish()
    await message.bot.send_message(message.from_user.id, "Создание документа отменено.")


async def step1(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["who_is"] = callback.data
        data["state"] = await state.get_state()
    await callback.bot.send_message(callback.from_user.id, "Введите дату создания договора: дд.мм.гггг",
                                    reply_markup=cancel_enter())
    await NewContract.next()


async def step2(message: types.Message, state: FSMContext):
    if check_date(message.text):
        async with state.proxy() as data:
            data["date"] = message.text
        await NewContract.next()
        await message.bot.send_message(message.from_user.id, "Адрес погрузки:",
                                       reply_markup=cancel_enter())
    else:
        await message.bot.send_message(message.from_user.id, "Неправильный формат даты!", reply_markup=cancel_enter())
        await NewContract.step1.set()


async def step3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["from_address"] = message.text
    await message.bot.send_message(message.from_user.id, "Введите дату и время погрузки:", reply_markup=cancel_enter())
    await NewContract.next()


async def step4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["from_date"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Контактное лицо, отвечающее за погрузку:", reply_markup=cancel_enter())


async def step5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact_person_from"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Номер контактного лица, отвечающего за погрузку:", reply_markup=cancel_enter())


async def step6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact_person_from_phone"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Введите адрес разгрузки: ", reply_markup=cancel_enter())


async def step7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["to_address"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Введите дату и адрес разгрузки", reply_markup=cancel_enter())


async def step8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["to_date"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Контактное лицо, отвечающее за погрузку:", reply_markup=cancel_enter())


async def step9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact_person_to"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Номер контактного лица, отвечающего за погрузку:", reply_markup=cancel_enter())


async def step10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact_person_to_phone"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Требуемый вид подвижного состава", reply_markup=cancel_enter())


async def step11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type_machine"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Наименование груза, объем и рамзмеры:", reply_markup=cancel_enter())


async def step12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_cargo"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Вид загрузки:")


async def step13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type_loading"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Вид выгрузки:")


async def step14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type_unloading"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Деньги для ЗАКАЗЧИКА:")


async def step15(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price_customer"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Деньги для ПЕРЕВОЗЧИКА:")


async def step16(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price_driver"] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Марка автомобиля:")


async def step17(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['car_model'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Гос. номер:")


async def step18(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cur_number'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Марка П./П.:")


async def step19(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['trailer_model'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Гос. номер П./П.:")


async def step20(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['trailer_model'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "ФИО водителя:")


async def step21(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_driver'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Номер телефона водителя:")


async def step22(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_driver'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Паспорт водителя:")


async def step23(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['passport_driver'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Контакты менеджера (твои):")


async def step24(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_manager'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Информация о ЗАКАЗЧИКЕ (ИП/ФИЗ и т.п.):")


async def step25(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_customer'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Сокращенное название организации ЗАКАЗЧИКА:")


async def step26(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['short_org_name_customer'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Полноне название организации ЗАКАЗЧИКА:")


async def step27(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_org_name_customer'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Информация о ПЕРЕВОЗЧИКЕ (ИП/ФИЗ и т.п.):")


async def step28(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['carrier_info'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Сокращенное название организации ПЕРЕВОЗЧИКА:")


async def step29(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['short_org_name_carrier'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Полное название организации ПЕРЕВОЗЧИКА:")


async def step30(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['short_org_name_carrier'] = message.text
    await NewContract.next()
    await message.bot.send_message(message.from_user.id, "Сбор информации закончен, идет обработка!")


def register_handler_new_contract(dp: Dispatcher):
    dp.register_message_handler(start_, commands=["new_contract"], state=None)
    dp.register_message_handler(start_, Text(equals="нк", ignore_case=True), state=None)
    dp.register_callback_query_handler(stop_, Text(equals="stop"), state='*')
    dp.register_callback_query_handler(step1, Text(equals='М', ignore_case=True), state=NewContract.step1)
    dp.register_message_handler(step2, content_types=["text"], state=NewContract.step2)
    dp.register_message_handler(step3, content_types=["text"], state=NewContract.step3)
    dp.register_message_handler(step4, content_types=["text"], state=NewContract.step4)

