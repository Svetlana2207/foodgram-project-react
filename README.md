# foodgram-project-react

![main.yml](https://github.com/Svetlana2207/foodgram-project-react/actions/workflows/main.yml/badge.svg)

#### Ссылка на проект: http://158.160.14.90/
####                   http://fooggram-ponomareva.ddns.net/


### Проект Fooodgram
Описание:
На сервисе "Продуктовый помощник" пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Как запустить проект в контейнере docker:

Заполнить переменные окружения .env:

- DB_ENGINE=
- DB_NAME=
- POSTGRES_USER=
- POSTGRES_PASSWORD=
- DB_HOST=
- DB_PORT=
- SECRET_KEY=

Запустить docker-compose командой:

docker-compose up -d --build

Собрать статику и выполнить миграции внутри контейнера, создать суперпользователя:

docker-compose exec backend python manage.py migrate --noinput

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input

наполнить базу данных из файла фикстур:

docker-compose exec backend python manage.py loaddata fixtures.json


### Деплой на удаленном сервере:

Для запуска на удаленном сервере необходимо:

перенести файлы docker-compose.yaml и nginx.conf на сервер, выполнив команду:

scp <название файла> <username>@<server_ip>:/home/username/

на github, в настройках репозитория Secrets --> Actions создать и заполнить переменные окружения:

- DOCKER_USERNAME # Имя пользователя на Docker Hub;
- DOCKER_PASSWORD # Пароль от Docker Hub;
- DB_ENGINE # Указать, что работаем с базой данных PostgresQl;
- DB_NAME # Имя базы данных;
- DB_HOST # Название контейнера базы данных; 
- DB_PORT # Порт для подключения к базе данных;
- POSTGRES_USER # Логин для подключения к базе данных;
- POSTGRES_PASSWORD # Пароль для подключение к базе данных;
- SECRET_KEY # Секретный ключ приложения;
- USER # Имя пользователя на сервере;
- HOST # Публичный IP-адрес сервера;
- PASSPHRASE # Указать в том случае, если ssh-ключ защищен фразой-паролем;
- SSH_KEY # Приватный ssh-ключ;
- TELEGRAM_TO # ID телеграм-аккаунта;
- TELEGRAM_TOKEN # Токен телеграм-бота.


После git push в главную ветку master:

- будут автоматически запускаться тесты проверки кода на соответствие стандарту PEP8 (с помощью flake8);
- сборка и доставка докер-образа на Docker Hub;
- автоматический деплой на боевой сервер;
- отправка сообщения в Telegram при успешном завершении деплоя.


### Aвтор: [Svetlana2207](https://github.com/Svetlana2207)
