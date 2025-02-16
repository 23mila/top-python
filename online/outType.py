#type(имя класса, кортеж родительских классов, словарь атрибутов)

Person = type("Person", (object,), {'greet': lambda self: f"hi, im {self.name}"})

person = Person()
person.name = 'a'
print(person.greet())
# ----------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} make sound"

Dog = type("Dog", (Animal, ), {"speak": lambda self: f"{self.name} гав"})

dog = Dog('dogg')
print(dog.speak())

# ----------------------------------------------------------------

Person = type("Person", (object,), {'age': 0})

person = Person()
person.age = 25

setattr(Person, "birthday", lambda self: f"с {self.age + 1} др")

print(person.birthday())
# ----------------------------------------------------------------

class MyMeta(type):
    def __new__(cls, name, *args, **kwargs):
        print(f"создание класса {name}")
        return super().__new__(cls, name, *args, **kwargs)


class Person(metaclass=MyMeta):
    pass
# ----------------------------------------------------------------

def class_factory(name, base_class, attributes):
    return type(name, (base_class, ), attributes)

NewClass = class_factory("NewClass", object, {'greet': lambda self: f"hi from newclass"})


new_instace = NewClass()
print(new_instace.greet())
# ----------------------------------------------------------------

data = {
    "class_name": "Employee",
    'attributes': {"name": '', "salary": 0},
    "methods": {
        "get_info": lambda  self: f"{self.name} earns {self.salary}"
    }
}

Employee = type(data['class_name'], (object, ), {**data['attributes'], **data["methods"]})

employee = Employee()
employee.name = 'a'
employee.salary = 5000

print(employee.get_info())
# ----------------------------------------------------------------
"""

создаем Car
type
атрибуты:
brand
model
Метод: 
description - выводит строку с описанием 
"""

"""
создаем Dog, наследуется от animal
animal имеет speak
dog должен переопределить speak
"""

""""
student
атрибуты: 
name
age

динамически добавить
get_details, с выводом информации о студенте
"""

"""
сделать фабрику create_class
принимает имя класса
атрибуты
методы
возвращает новый класс

создайте Teacher:
атрибуты name, subject
метод introduce с информацией
, Course
атрибуты: course_name, duration
метод info  выводит информацию

"""

"""
мета LoggerMeta
выводит информацию в консоль при создании любого класса

на основе Employee, имеет name и position
"""