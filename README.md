# Телеграм Бот для магазина книг.
![Магазин Книг](images/МК.png)
## 1. Команды бота.
Бот отвечает на следующие команды:
*  /start  - Вызывает панель клиента с информацией.
*  /moderator  - Вызывает панель модератора для работы с базой данных
После ввода одной из команд бот отправляет панель в личные сообщения пользователя.
## 2. Функционал.
После ввода команды  /start  у пользователя появляется панель с информацией о товаре и работе магазина и его расположения.
![Панель пользователя](images/ПП.png)
В панели пользователя есть три команды:
*  /Режим работы  - Выводит информацию о времени работы
*  /Расположение  - Выводит адрес магазина
*  /Книги  - Выводит список имеющихся книг в магазине
![Пример команд](images/ПК.png)
 
 
 
 
 
 
Команда  /moderator  предназначена для модераторов магазина и открывает доступ к добавлению и удалению информации из базы данных магазина.
![Панель модератора](images/ПМ.png)
В панели модератора есть команды:
*  /Загрузить  - Загружает информацию о книге в базу данных
*  /Удалить  - Удаляет информацию о книге из базы данных
 

![Пример загрузки](images/ПЗ.png)
 
 
![Пример удаления](images/ПУ.png)
 
Дополнительно:
Для корректной работы команды  /moderator  нужно создать группу в телеграмме и сделать в нем бота админом.
Для работы бота необходимо иметь установленную библиотеку aiogram.
Для её установки воспользуйтесь командой: pip install aiogram.
 
 
