from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import Message

API_TOKEN = '5595500871:AAFJqccOSaG3fcRP5-Ew5xb1gLMrWcjNMec'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

array_keyboard = [1, 2]


async def send_to_admin(dp):
    await bot.send_message(chat_id=5595500871, text='Bot start')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print("chat_id:", message.chat.id)
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text='Hello!', reply_markup=keyboard_markup)


if __name__ == '__main__':
    executor.start_polling(dp)
