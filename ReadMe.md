# Приложение для реализации древовидного меню
## Развертывание виртуальной среды
`python -m venv venv` - создание виртуальной среды
### Windows
`venv\Scripts\activate` - активация виртуальной среды
### Linux
`source venv/bin/activate` - активация виртуальной среды
## Установка зависимостей
`pip install -r requirements` - установка зависимостей
## Применене миграций
`python manage.py migrate` - применение миграций
## Создание админа
`python manage.py createsuperuser` - создание админа(после выполнения данной команды следуйте инструкциям в терминале)
## Запуск сервера
`python manage.py runserver` - запуск сервера