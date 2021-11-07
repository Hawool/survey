#Survey
API для системы опросов пользователей.

Функционал для администратора:
- авторизация в системе
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователя:
- получение списка активных опросов
- прохождение опроса; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов

Документация по API представлена на странице http://0.0.0.0:8000/swarreg

Иструкция по запуску:
- git clone git@github.com:Hawool/survey.git
- cd survey
- docker-compose build
- docker-compose run api python manage.py makemigrations
- docker-compose run api python manage.py migrate
- docker-compose run api python manage.py createsuperuser # требуется ввести username и password
- docker-compose up

Затем можно открыть в браузере http://0.0.0.0:8000