# likesoft-library

## Описание функциональности
Апи библиотеки

###### Для запуска необходимы docker и docker-compose
###### [Инструкции по установке докера](https://docs.docker.com/engine/install/)

Склонировать репозиторий
```bash
git clone https://github.com/jingleMyBells/likesoft-library.git
```

Перейти в каталог с проектом и конфигурационным файлом развертки
```bash
cd likesoft-library/deploy
```

Создать .env файл
```bash
cat env_example.txt > .env
```

Запустить проект
```bash
  docker-compose up
```

## API Endpoints:
- [GET/POST/PATCH/DELETE: books](http://localhost/books/)
- [POST: users](http://localhost/users/)


#### Стэк
Python3.11.2, Django REST Framework, Celery, Nginx, Docker, MySQL, Pytest

###### Заметки:
- модель пользователя не переопределена, тк модель "из коробки" предоставляет все необходимые поля.
в связи с этим нет и тестов для юзера (а интеграционные тесты со сторонними почтовыми сервисами кажутся чрезмерными в рамках тестового)
- контейнеры стартую немного долго - это корректное поведение, тк бэкенд дожидается healthcheck базы данных
- отправка почтового сообщения сознательно идет в консоль (впрочем, об этом чуть выше сказано), обработка исключений в связи с этим опущена
- https://github.com/jingleMyBells/likesoft-library/pull/1 - пуллреквест фичи
- https://github.com/jingleMyBells/likesoft-library/pull/2 - пуллреквест "фиксов"

