# Cars API
RESTful API для сбора данных об автомобилях и фильтрации по различным параметрам.

## Функции
1. Добавление нового автомобиля:
- Марка - Brand
- Модель - model
- Год выпуска - year
- Тип топлива (бензин, дизель, электричество, гибрид) - fuel_type
- Тип КПП (механическая, автоматическая, вариатор, робот)
- Пробег - mileage
- Цена - price

2. Получение списка автомобилей с фильтрами:
- По марке
- По модели
- По типу топлива
- По типу 
- По году выпуска (одно число или диапазон) - year, min_year, max_year
- По пробегу (диапазон) - min_mileage, max_mileage
- По цене (диапазон) - min_price, max_price

3. Аутентификация и авторизация пользователей:
 - Basic аутентификация
 - Незарегистрированные пользователи могут видеть список автомобилей и отфильтровать его
 - Зарегистрированные пользователи с флагом is_staff = True могут изменять и дополнять список автомобилей

4. Пагинация для списка:

- По умолчанию 10 элементов на страницу.

Пример ответа:
```json
{
  "count": 15,
  "next": "http://127.0.0.1:8000/api/cars/?page=2",
  "previous": null,
  "results": [
    {
      "id": 15,
      "brand": "McLaren",
      "model": "MP4/4",
      "fuel_type": "бензин",
      "transmission": "механическая",
      "year": 1988,
      "mileage": 5000,
      "price": 4800000
    }
  ]
}
```

4. Документация swagger

## Установка

### Клонирование репозитория
```commandline
git clone https://github.com/username13121/cars-api.git
```

### Установка пакетов
```commandline
cd cars-api
pip install -r requiriments.txt
```

### Миграции django
```commandline
python manage.py migrate
```

### Создание суперпользователя
```commandline
python manage.py createsuperuser
```

### Запуск сервера
```commandline
python manage.py runserver
```

## Документация
Swagger: http://127.0.0.1:8000/docs
