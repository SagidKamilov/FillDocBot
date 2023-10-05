from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings import TOKEN


def _on_startup(dp: Dispatcher):



def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())
    executor.start_polling(dispatcher=dispatcher, skip_updates=True, on_startup=_on_startup(dp=dispatcher))
