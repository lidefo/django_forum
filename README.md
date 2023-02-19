# django_forum
## [In English](##English documentation) | [In Russian](##Документация на русском)

## English documentation

## Project description

The essence of this project is to apply the skills acquired during the training in practice. It is a small forum, 
with the ability to create users, threads and messages.

### What is implemented in this project?

- Custom users.
- Authorization.
- DataBase based on PostgreSQL.
- Admin panel.
- Unauthorized users can't create message and threads.

## Development tools:

- Python 3.10
- Django 4.1
- PostgreSQL

## How to launch:

1) Clone repository
```
git clone "repository_link"
```

2) Create virtual environment
```
python -m venv venv
```

3) Activate virtual environment
```
venv\Scripts\activate.bat
```


4) Install requirement libraries
```
pip install -r requirements.txt
```

5) Create DataBase based on PostgreSQL

6) Fill .env.example file and rename it to ".env"

7) Apply migrations
```
python manage.py migrate
```

8) Launch server

```
python manage.py runserver
```
## **P.S**
### [API](https://github.com/lidefo/django_forum_api)

## Документация на русском
## Описание проекта:


Суть данного проекта в том, чтобы применить навыки, полученные во время обучения на практике.
Он из себя представляет небольшой форум, с возможностью создания пользователей, тредов и сообщений.

### Что реализовано в проекте?

- Кастомные пользователи.
- Система авторизации.
- База данных на PostgreSQL.
- Админ-панель.
- Невозможность создания тем и сообщений неавторизованным пользователям.

## Инструменты разработки:

- Python 3.10
- Django 4.1
- PostgreSQL

## Запуск проекта:

1) Клонировать репозиторий
```
git clone ссылка_на_репозиторий
```

2) Создать виртуальное окружение
```
python -m venv venv
```

3) Активировать виртуальное окружение

```
venv\Scripts\activate.bat
```

4) Установить необходимые библиотеки
```
pip install -r requirements.txt
```

5) Создать базу данных PostreSQL с названием **"forum_db"**

6) Создать и заполнить файл .env

```
DJANGO_SECRET_KEY=
DB_PASS=
DB_USER=
```

7) Выполнить миграции
```
python manage.py migrate
```

8) Запуск сервера

```
python manage.py runserver
```

## **P.S**
### [API](https://github.com/lidefo/django_forum_api)