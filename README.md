# Лаунчер для GDS на Python

Это лаунчер написанный на Python с использованием библиотеки [Flet](https://flet.dev/) для запуска, обновления и взаимодействия с ReGDS (ReMeow Geometry Dash Server).

## Функционал

- Проверка наличия интернет соединения
- Отображение новостей с сервера
- Получение данных о топ игроках и креаторах
- Проверка обновлений лаунчера
- Проверка обновлений сервера
- Скачивание и установка клиента GDPS
- Запуск клиента GDPS
- Обновление лаунчера 
- Изменение настроек - читы, моды, текстурпаки
- Интеграция с Discord Rich Presence

## Важные функции

**`check_internet_connection()`** - проверяет наличие интернет соединения.

**`get_news()`** - получает последние новости с сервера.

**`on_update()`** - проверяет нужно ли обновление GDPS.

**`download_regds()`** - скачивает и устанавливает GDPS.

**`open_regds()`** - запускает GDPS.

**`update_launcher()`** - обновляет лаунчер до последней версии.

**`discord_rpc()`** - настраивает статус в Discord.

## Важные переменные

**`temp_folder_path`** - путь к папке для временных файлов. 

**`new_version`** - хранит новую версию лаунчера при проверке обновлений.

**`version`** - текущая версия лаунчера.

**`topic`, `avatar`, `description`** - данные последних новостей с сервера.

**`CLIENT_ID`** - идентификатор для Discord Rich Presence.

## Используемые библиотеки

- [Flet](https://flet.dev/) - для построения интерфейса
- Requests - для запросов к API сервера
- Asyncio - для асинхронных операций
- Subprocess - для запуска процессов
- Shutil - для копирования файлов
- Pypresence - для Discord RPC

## Как запустить

1. Установить зависимости `pip install -r requirements.txt`

Лаунчер готов к работе!, если вы используете лаунчер для своего сервера, то укажите в качестве автора ReMeow :3
