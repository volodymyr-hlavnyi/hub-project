# Задача: порекомендовать фильмы
# в определенной категории.
# Напишите программу, которая запрашивают информацию
# у пользователя, делает запросы в базу
# данных и выводит результат.
# Работаем с базой данных фильмов Sakila.
#
# 1 .При запуске программы выводится список категорий
# (номер и название категории)

# 2. Пользователь может ввести номер категории

# 3. Программа выводит все фильмы в данной категории,
# но не более 10 фильмов. О фильме
# выводится следующая информация:
# название, год выпуска, описание.
# Опционально - список актеров.

# 4. * Поменяйте программу так, чтобы на шаге 1
# пользователь мог выбрать поиск по категории
# или по имени актера.
#
# Если выбирается поиск по категории,
# то выводится список категории
# и уже описанный поиск по категории.
#
# Если выбирается поиск по актеру, то сначала
# пользователь вводит имя пользователя и
# делается поиск по базе актеров. Если указанный
# пользователем актер существует,
# то можно выбрать имя из предложенных вариантов и
# найти все фильмы с участием этого актера.
# В запросе для поиска по указанному имени
# актера можно пользоваться select/like чтобы убедиться,
# что актер(ы) с таким или похожим
# именем существуют в базе, прежде чем
# искать фильмы по имени актера.


from hw.hw_37 import Connector
from SakilaTools import SakilaTools

dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'sakila',
}

db = Connector(dbconfig)
if int(input("Choose method: 1 - by category, 2 - by actor: ")) == 2:
    name = input("Enter actor name: ")
    actors = SakilaTools.get_actors_by_name(db.cursor, name)
    for i, actor in enumerate(actors):
        print(i, actor)
    actor_index = input("Enter actor index: ")
    actor_id = actors[int(actor_index)].id
    films = SakilaTools.get_films_by_actor(db.cursor, actor_id)
    for i, film in enumerate(films):
        print(i, film)
    film_index = input("Enter film index: ")
    print(films[int(film_index)].description)
else:
    dict_categories = SakilaTools.get_categories(db.cursor)
    for key, value in dict_categories.items():
        print(key, value)
    cat_number = input("Enter category number: ")
    films = SakilaTools.get_films_by_category(db.cursor, cat_number, 2)
    for i, film in enumerate(films):
        print(i, film)
    film_index = input("Enter film index: ")
    print(films[int(film_index)].description)
