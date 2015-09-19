# django_task
В проекте использовал `Django 1.8`, `python3`, `sqlite`. Реализовал функционал записи к нескольким врачам, для теста создал 2 врача, есть возможность выбрать день и время, ввести свои ФИО. Время только с 9:00 до 17:00. Выбрать выходные нет возможности. `views.py` отвечает за невозможность записаться в одно и то же время к одному врачу. 
## Как запустить на ubuntu server 14.04:
- `sudo ./start.sh` 

Этот скрипт должен установить все необходимые пакеты, клонировать данный репозиторий и запустить сервер на 80 порту. По `0.0.0.0:80` откроется стартовая страница с формой для данных, по `0.0.0.0:80/allapps` доступен только для админа список всех записей по запросу из `sqlite`, если пользователь не аутентифицирован, то он доступ не получит . Админка доступна по `/admin`. login `admin`, passwd `admin`.

Если Вы хотите очистить бд, то из корня проекта необходимо:
- `sqlite3 db.sqlite3`
- `delete from clinic_appointment;`

