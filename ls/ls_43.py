from datetime import datetime


class Car:
    def __init__(self, model, color, year):
        self.color = color
        self.model = model
        self.year = year

    def __str__(self):
        return f'Model: {self.model} color: {self.color} year: {self.year}'


def get_car_by_color(list_car, color):
    return filter(lambda x: x.color == color, list_car)


car1 = Car('BMW', 'black', 2020)
car2 = Car('Audi', 'white', 2021)
car3 = Car('Toyota', 'red', 2019)
car4 = Car('Ford', 'blue', 2018)
car5 = Car('Kia', 'yellow', 2017)
car6 = Car('Mazda', 'green', 2016)
car7 = Car('Nissan', 'orange', 2015)
car8 = Car('Lexus', 'purple', 2014)
car9 = Car('Honda', 'pink', 2013)
car10 = Car('Chevrolet', 'brown', 2012)

cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

for car in get_car_by_color(cars, 'black'):
    print(car)


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __str__(self):
        return f'Name: {self.name} birth_date: {self.birth_date}'


person1 = Person('John', '1990-01-01')
person2 = Person('Anna', '1995-01-01')
person3 = Person('Tom', '2000-01-01')
person4 = Person('Alice', '2005-01-01')
person5 = Person('Bob', '2010-01-01')
person6 = Person('Kate', '2015-01-01')
person7 = Person('Jack', '2020-01-01')
person8 = Person('Liza', '2015-01-01')
person9 = Person('Mike', '1980-01-01')
person10 = Person('Sara', '1974-01-01')
persons = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]


class Employee(Person):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        # self.a = None
        self._get_by_date_year()

    def _get_by_date_year(self):
        self.age = datetime.now().year - datetime.strptime(self.birth_date, '%Y-%m-%d').year

    def __str__(self):
        return f'Name: {self.name} age: {self.age}'

    def is_valid_age(self):
        return self.age >= 18


employees = [Employee(per.name, per.birth_date) for per in persons]

for employee in employees:
    print(employee, employee.is_valid_age())
