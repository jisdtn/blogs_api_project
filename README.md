### API для платформы с блогами

### В чем польза

```commandline
REST API для сервиса с блогами,
где пользователи могут подписываться на авторов,
оставлять комментарии и писать собственные посты.
```
### Запуск проекта в dev-режиме:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/jisdtn/blogs_api_project
```

```
cd blogs_api_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов к API.

```commandline
http://127.0.0.1:8000/api/v1/groups/{id}/
```
```commandline
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
```commandline
http://127.0.0.1:8000/api/v1/post/ (POST)
```
