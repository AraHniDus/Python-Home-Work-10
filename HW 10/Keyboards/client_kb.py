from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Книги')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1).row(b2, b3)


