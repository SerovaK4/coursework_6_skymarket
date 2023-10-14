# Доска объявлений

## Стек технологий
- Dgango
- PostgreSQL
- Git
- CORS

### В бэкенд-части проекта был реализован следующий функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.


## Настройка

Первое, что нужно сделать, это клонировать репозиторий:

    $ git clone https://github.com/gocardless/sample-django-app.git
    $ cd sample-django-app

Создайте виртуальную среду для установки зависимостей и активируйте ее:

    $ virtualenv2 --no-site-packages env
    $ source env/bin/activate

Затем установите зависимости:

    (env)$ pip3 install -r requirements.txt

## Настройка переменных окружения
Для работы с переменными окружениями необходимо в проекте создать файл .env и заполнить его по типу файла .env.example:

DB_ENGINE=django.db.backends.engine

DB_NAME=skymarket

DB_USER=skymarket

DB_PASSWORD=skymarket

DB_HOST=localhost

DB_PORT=5432

EMAIL_HOST=smtp.gmail.com

EMAIL_HOST_USER=example@gmail.com

EMAIL_HOST_PASSWORD=password

EMAIL_PORT = 587
