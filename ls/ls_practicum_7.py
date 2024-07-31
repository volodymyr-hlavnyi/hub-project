from abc import ABC, abstractmethod
from enum import Enum


class Seasons(Enum):
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'
    WINTER = 'winter'

    def __str__(self):
        return self.name.capitalize()


class Plant(ABC):
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.height = 0

    @abstractmethod
    def grow_per_season(self):
        pass

    @staticmethod
    def do_spring(self):
        pass

    @staticmethod
    def do_summer(self):
        pass

    @staticmethod
    def do_autumn(self):
        pass

    @staticmethod
    def do_winter(self):
        pass

    def __str__(self):
        return f'{self.name} age: {self.age} height: {self.height}'

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

    def do_winter(self):
        self.age += 0.25
        self.height += 0

    def do_spring(self):
        self.age += 0.25
        self.height += 2

    def do_summer(self):
        self.age += 0.25
        self.height += 1

    def do_autumn(self):
        self.age += 0.25
        self.height -= 1

    def grow_per_season(self):
        self.do_spring()
        self.do_summer()
        self.do_autumn()
        self.do_winter()




class Tree(Plant):
    def __init__(self, name):
        super().__init__(name)

    def do_winter(self):
        self.age += 0.25
        self.height += 0

    def do_spring(self):
        self.age += 0.25
        self.height += 2

    def do_summer(self):
        self.age += 0.25
        self.height += 2

    def do_autumn(self):
        self.age += 0.25
        self.height -= 1

    def grow_per_season(self):
        self.do_spring()
        self.do_summer()
        self.do_autumn()
        self.do_winter()






rose = Flower('Rose')
oak = Tree('Oak')
print(rose)
print(oak)

for y in range(6):
    rose.grow_per_season()
    oak.grow_per_season()

print(rose)
print(oak)
