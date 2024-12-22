# Проект "Ресторан История Вкуса"

Данный проект является сайтом, дающий возможность клиентам бронировать столы,
ознакамливаться с меню и с самим рестораном.

Также данный сайт позволит сотрудникам стать более эффективнее, поскольку
на сайте можно:

- Контролировать бронь клиентов
- Быстро узнавать имя клиента и способы связи с ним (в случае опоздания)
- Редактировать кол-во и характеристик столов (кол-во мест, вип статус, статус занятости)

В сайте заложен следующий функционал:

- За час до начала брони отправляется предупредительное письмо на почту клиента (при небольшом капиталовложении можно сделать оповещение по SMS)
- Если бронь истекает, бронь удаляется, перед этим вся его информация сохраняется в папке logs/, а стол становится свободным
- Люди, не являющиеся сотрудниками ресторана, не имеют доступ к функциям сотрудников

Есть кастомная команда позволяющая создавать суперюзера: python manage.py csu

Для запуска celery, выполняющий главный функционал сайта, запустите следующие комманды:

- celery -A config worker -l INFO
- celery -A config beat -l INFO

Для быстрого запуска docker-compose:
- docker-compose up -d --build

Перечень переменных в .env:
- DB_NAME
- DB_USER
- DB_PASSWORD
- LANGUAGE_CODE
- TIME_ZONE
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- CACHE_ENABLED
- CACHE_LOCATION
- EMAIL_HOST
- EMAIL_PORT
- SECRET_KEY
