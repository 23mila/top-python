# 1 архитектурные паттерны
# 2 паттерны проектирования
# 3 идиомы

# mvc model view controller (1)
"""
model
управление данными/бизнес логика
хранение/извлечение/обработка данных
ORM

view
отображение
html/css/js
получаем данные от модели через контроллер

controller
управляет взаимодействием между моделью и представлением
http


"""
"""
разделение ответственности
модульность
масштабируемость
тестируемость
гибкость
упрощение разработки
"""

#ORM
"""
(фреймворки)
django
flask

pyramid
"""
"""
/src
    -контроллеры
    -модели
    -представления
    -core           - классы для управления MVC
    -config.py      - конфигурация приложения
    -Main.py        - точка входа в приложение 
"""
