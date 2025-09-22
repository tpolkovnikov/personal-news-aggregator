

Как зайти в вирутальное окружение:
 - Зайти в папку backend
 - Выполнить команду: `venv\Scripts\activate`

 Если в приглашении строки появилось (venv) - всё отлично!

 Для установки нужных зависимостей прописать: `pip install -r requirements.txt`
 Для записи актуальных зависимостей в файл прописать: `pip freeze > requirements.txt`

 Чтобы выйти из окружения: `deactivate`




Настройка Yandex GPT:

https://yandex.cloud/ru/docs/cli/quickstart#windows_1
- установить Интерфейс командной строки Yandex Cloud (CLI)

Запустить в командной строке windows: `iex (New-Object System.Net.WebClient).DownloadString('https://storage.yandexcloud.net/yandexcloud-yc/install.ps1')`
- Выбрать Y (Добавить yc в PATH)

Получение токена:
Получить OAuth токен на странице: https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb

Выполнить команду `yc config set token <OAuth>`
Выполнить команду `yc iam create-token`
- Записать полученный токен в переменную


