# Menu

## Описание
Это тестовое задание, представляющее из себя вэб-приложение с разветвленным меню. С [тестовым заданием](ТЗ.txt) можно
ознакомиться тут. Приложение имеет одну сущность:
### Menu
Имеет имя и может иметь родителя. Родителем может выступать другое меню. Таким образом реализуется вложенность.

## Стек
+ Python 3.10
+ Django 4.1

## Карта
- '' - страница объединяющая 2 стартовых меню из заранее созданных.
- '/menu/<id меню>' - страница для просмотра конкретного меню.

## Установка
1. Скопируйте проект: `git clone https://github.com/sergeytompson/menu_test_task`
2. Перейдите в папку проекта: `cd menu_test_task`
3. Запустите проект: `docker-compose up`

## Фикстуры
Для удобства ознакомления с проектом, при его запуске БД будет автоматически заполнена данными о 86 меню.
### Superuser
Для работы с административной частью проекта необходимо авторизаваться на странице '/admin/' с помощью логина
'superuser' и пароля 'superpassword'.

## Контакты
+ Telegram: @sergeytompson
+ Email: gfhfahfp@gmail.com