from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print('I can run and walk')

class Snake(Animal):
    def move(self):
        print('I can crawl')

class Dog(Animal):
    def move(self):
        print('I can bark')

class Lion(Animal):
    def move(self):
        print('I can roar')

R = Human
R.move()