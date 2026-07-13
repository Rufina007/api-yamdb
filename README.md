# YaMDb

Платформа для сбора отзывов на произведения: фильмы, книги, музыку.

# Описание

API позволяет пользователям оставлять отзывы и оценки произведениям, объединённым по категориям и жанрам. На основе оценок формируется рейтинг произведения.

# Стек технологий

Python 3.12
Django 5.1.1
Django REST Framework 3.15.2
djangorestframework-simplejwt
SQLite

# Развёртывание проекта

Клонировать репозиторий:

```bash
git clone git@github.com:Rufina007/api-yamdb.git
cd api-yamdb
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
cd api_yamdb
python3 manage.py migrate
```

Запустить сервер:

```bash
python3 manage.py runserver
```

# Импорт данных из CSV

Тестовые данные находятся в директории `api_yamdb/static/data/`.

Для загрузки данных в базу выполнить в папке `api_yamdb`:

```bash
python3 manage.py import_csv
```

Для доступа к админ-панели создать суперпользователя:

```bash
python3 manage.py createsuperuser
```

# Документация API

После запуска сервера документация доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

# Примеры запросов

# Регистрация:

```
POST /api/v1/auth/signup/
{
    "username": "ivan",
    "email": "ivan@example.com"
}
```

# Получение токена:

```
POST /api/v1/auth/token/
{
    "username": "ivan",
    "confirmation_code": "<код из письма>"
}
```

# Список произведений:

```
GET /api/v1/titles/
```

# Добавить отзыв:

```
POST /api/v1/titles/{title_id}/reviews/
{
    "text": "Отличный фильм",
    "score": 9
}
```

# Авторы

Rufina007     https://github.com/Rufina007
Mariaasme     https://github.com/Mariaasme
knoxforge702  https://github.com/knoxforge702
