## Инкапсуляция ##
class Animal:
    def __init__(self, name: str, age: int):
        self.__name = name      # приватное свойство
        self.__age = age        # приватное свойство

    # --- get и set через property ---
    @property
    def name(self):
        """Имя можно только прочитать, но не изменить"""
        return self.__name

    @property
    def age(self):
        """Возраст можно получить..."""
        return self.__age

    @age.setter
    def age(self, value: int):
        """...но при установке проверяем корректность"""
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = value

    def speak(self):
        print("Животное издаёт звук")

    def info(self):
        print(f"{self.__name}, возраст {self.__age}")


## Наследование ##
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str = "mongrel"):
        super().__init__(name, age)
        self.breed = breed # уникальное свойство

    def speak(self):
        print(f"{self.name} говорит: Гав-гав!")

    def move(self):
        print(f"{self.name} бежит на четырёх лапах")


class Bird(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} поёт: Чирик-чирик!")

    def move(self):
        print(f"{self.name} летит")


## Полиморфизм ##
animals: list[Animal] = [Dog("Шарик", 3), Bird("Снигирь", 2)]

for a in animals:
    a.speak()   # один вызов — разное поведение!

## Абстракция ##
from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def perform(self, animal):
        pass

class Feeding(Service):
    def perform(self, animal):
        print(f"{animal.__class__.__name__} покормлен.")

class Walking(Service):
    def perform(self, animal):
        print(f"{animal.__class__.__name__} выгулян.")
