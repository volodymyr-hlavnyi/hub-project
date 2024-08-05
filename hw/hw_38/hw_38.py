# В базе данных ich_edit три таблицы.
#
# Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и
# Sales с полями (sid, id, pid).
#
# Написать мини-интерфейс к базе данных, который умеет выполнять разные команды.

# 1. Выбрать таблицу для запроса. Предусмотреть возможность выбрать несколько таблиц.
# Вывести результат их соединения, если это возможно, или сообщение об ошибке.

# 2. Выбрать одно поле из выбранной таблицы и искомое значение этого поля. Вывести все
# подходящие строки

import dotenv
import os
from Connector import Connector
from IchEditTools import Ich_Edit

dotenv.load_dotenv()
ICH_HOST = os.getenv("ICH_HOST")
ICH_PASSWORD = os.getenv("ICH_PASSWORD")
ICH_USER = os.getenv("ICH_USER")
ICH_DATABASE = os.getenv("ICH_DATABASE")

dbconfig = {
    'host': f"{ICH_HOST}",
    'user': f"{ICH_USER}",
    'password': f"{ICH_PASSWORD}",
    'database': f"{ICH_DATABASE}",
}


def get_list_from_table():
    pass


def select_table():
    pass


if __name__ == '__main__':

    db = Connector(dbconfig)
    list_of_tables = {
        'Users': ['id', 'name', 'age'],
        'Sales': ['pid', 'prod', 'quantity'],
        'Products': ['sid', 'pid', 'id']
    }
    for num, tb in enumerate(list_of_tables):
        print(f" {num} - {tb}")
    num_table = int(input('Select table for view records: '))
    if num_table == 0:
        for num, record in enumerate(Ich_Edit.get_users(db.cursor)):
            print(f" {num} - {record}")
    elif num_table == 1:
        for num, record in enumerate(Ich_Edit.get_sales(db.cursor)):
            print(f" {num} - {record}")
    elif num_table == 2:
        for num, record in enumerate(Ich_Edit.get_products(db.cursor)):
            print(f" {num} - {record}")

    db.close()
