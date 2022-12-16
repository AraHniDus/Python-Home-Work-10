from aiogram import types, Dispatcher
from create_bot import dp, bot
from Keyboards import kb_client
from Data_base import Book_db

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет увлекательного чтения!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/HomeWorkPy10_bot')

@dp.message_handler(commands=['Режим_работы'])
async def book_open_comand(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10:00 до 19:00, Сб-Вс с 10:00 до 16:00')

@dp.message_handler(commands=['Расположение'])
async def book_place_comand(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Ломоносова 15')

@dp.message_handler(commands=['Книги'])
async  def book_select_command(message : types.Message):
    await Book_db.sql_read(message)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(book_open_comand, commands=['Режим_работы'])
    dp.register_message_handler(book_place_comand, commands=['Расположение'])
    dp.register_message_handler(book_select_command, commands=['Книги'])

