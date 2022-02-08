from aiogram import types, Dispatcher, executor, Bot
from generate import print_all
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, это бот для генератора случайных личностей \n \n'
                         '/generate - сгенирировать')


@dp.message_handler(commands=['generate'])
async def generator(message: types.Message):
    await message.answer(print_all())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
