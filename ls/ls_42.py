# Дополнить класс Person
# операцией сложения.
# При сложении двух объектов этого класса
# операция должна возвращать
# новый объект класса Person,
# у которого рост - четверть от среднего
# арифметического роста родителей,
# вес - двадцатая часть от среднего
# арифметического веса родителей,
# год рождения - текущий.
#
# Дополнительно придумать
# и определить методы _len_, _bool_.

class Person:
    def __init__(self, height, weight, birth_year):
        self.height = height
        self.weight = weight
        self.birth_year = birth_year

    def __add__(self, other):
        return Person((self.height + other.height) / 2 / 4, (self.weight + other.weight) / 2 / 20, 2024)

    def __str__(self):
        return f'Person: height={self.height}, weight={self.weight}, birth_year={self.birth_year}'

    def __len__(self):
        return int(round(self.height, 0))

    def __bool__(self):
        return self.weight > 0


person_dad = Person(180, 80, 1990)
person_mam = Person(150, 55, 1980)
baby = person_dad + person_mam
print(baby)
print(len(baby))
print(bool(baby))
