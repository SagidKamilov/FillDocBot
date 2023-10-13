import os

from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from Bot import settings
from Bot.handlers import register_contract_start, register_handler_new_contract, register_handler_delete_contract


def _on_startup(dp: Dispatcher):
    register_contract_start(dp)
    register_handler_new_contract(dp)
    register_handler_delete_contract(dp)


def main():
    bot = Bot(token=settings.TOKEN, parse_mode='HTML')
    dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())
    executor.start_polling(dispatcher=dispatcher, skip_updates=True, on_startup=_on_startup(dp=dispatcher))
