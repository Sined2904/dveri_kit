# Dveri_kit

### Описание
Бэк для сайта, на котором продаются двери. 




### Технологии
asgiref==3.7.2
Django==4.2.8
django-ckeditor==6.7.0
django-js-asset==2.1.0
Pillow==10.1.0
python-dotenv==1.0.0
sqlparse==0.4.4
typing_extensions==4.8.0
tzdata==2023.3

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Заполните файл .env
- В корневой папке проекта выполните команду:
```
docker compose up 
```

### Описание переменных окружения
POSTGRES_DB - название БД
POSTGRES_USER - имя пользователя БД
POSTGRES_PASSWORD - пароль пользователя БД
DB_NAME - название БД
DB_HOST - адрес БД
DB_PORT - порт БД
SECRET_KEY - криптографическая подпись Django
DEBUG - статус режима дебаг


### Авторы
Нестеренко Никита
Сашкина Кристина
Соловьев Эдуард
Пиневич Денис


Github - Sined2904
Den2904@yandex.ru
TG - @PinevichD