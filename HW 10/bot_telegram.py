from aiogram.utils import executor
from create_bot import dp
from Data_base import Book_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    Book_db.sql_start()

from Handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

