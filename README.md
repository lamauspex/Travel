# Карта интересных мест Москвы

**Django REST API для интерактивной карты активного отдыха**

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14.0-red.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

Бэкенд для проекта Артёма - популярного блогера, создающего интерактивную карту уникальных мест Москвы для активного отдыха.

## 🟢 О проекте

Проект представляет собой REST API для веб-приложения, которое отображает на карте Москвы интересные места для активного отдыха. 
В отличие от стандартных агрегаторов, здесь собраны уникальные локации, известные только местным жителям.

### Особенности

**Умная фильтрация:** по категориям и поиск по названию/описанию
**GeoJSON поддержка:** для легкой интеграции с картами
**Загрузка изображений:** для каждой локации
**Удобная админка:** с модерацией контента
**REST API:** с пагинацией и поиском


##  🟢 Быстрый старт

### 1. Клонирование и настройка окружения

#### Создание виртуального окружения
```bash
python -m venv travel_map_env
```
#### Активация окружения
 Windows:
```bash
travel_map_env\Scripts\activate
```
 Linux/MacOS:
```bash
source travel_map_env/bin/activate
```

#### Установка зависимостей
```bash
pip install -r requirements.txt
```


### 2. Настройка базы данных
#### Применение миграций
```bash
python manage.py migrate
```
#### Создание суперпользователя
```bash
python manage.py createsuperuser
```
#### Загрузка тестовых данных
```bash
python manage.py loaddata categories.json
```


### 3. Запуск сервера
```bash
python manage.py runserver
```
Приложение будет доступно по адресу: http://127.0.0.1:8000/



### 4. Тестирование

### Запуск тестов
#### Стандартные Django тесты
```bash
python manage.py test
```
#### С подробным выводом
```bash
python manage.py test --verbosity=2
```
#### Только определенное приложение
```bash
python manage.py test locations
```
#### С покрытием кода (требуется pytest-cov)
```bash
pytest --cov=.
```

## Административная панель
Доступна по адресу: /admin/

Возможности админки:

 - Управление категориями и локациями
 - Модерация новых локаций
 - Загрузка фотографий
 - Просмотр статистики


## Модели данных

**Location (Локация)**
name - Название локации
description - Подробное описание
address - Физический адрес
latitude/longitude - Геокоординаты
category - Категория локации
photo - Фотография места
is_approved - Статус модерации

**Category (Категория)**
name - Название категории
description - Описание категории
icon - Emoji-иконка для отображения



## 🟢 Технологический стек

Backend:

 Django 4.2 - основной фреймворк
 Django REST Framework - REST API
 Pillow - работа с изображениями
 CORS Headers - кросс-доменные запросы


База данных:

SQLite (разработка) / PostgreSQL (продакшн)


Фронтенд-готовность:

GeoJSON формат для карт
REST API с фильтрацией
Media files поддержка

Ваш вклад в проект приветствуется! Если вы хотите внести изменения или улучшения, создайте pull request или откройте issue на GitHub.

#### Контакты
Если у вас есть вопросы или предложения, не стесняйтесь связаться со мной:

- Имя: Резник Кирилл
- Email: lamauspex@yandex.ru
- GitHub: https://github.com/lamauspex
- Telegram: @lamauspex

Спасибо за интерес к проекту! Надеюсь, он будет полезен в вашей работе.
