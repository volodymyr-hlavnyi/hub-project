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


from IchEditTools import Ich_Edit
from Connector import Connector
from get_db_config import get_db_config



if __name__ == '__main__':

    db = Connector(get_db_config())
    dict_of_tables = {
        'Exit': [],
        'users': ['id', 'name', 'age'],
        'sales': ['pid', 'prod', 'quantity'],
        'product': ['sid', 'pid', 'id']
    }
    list_kind_view = [
        'Exit',
        'View Records of table',
        'View list of Column of table',
        'Search value'

    ]
    while True:

        # 1
        for num, tb in enumerate(list_kind_view):
            print(f" {num} - {tb}")
        num_kind_view = int(input('Select type of view (0 - exit)): '))

        # 2
        for num, tb in enumerate(dict_of_tables):
            print(f" {num} - {tb}")
        num_table = int(input('Select table (0 - exit): '))

        # 3
        if num_kind_view == 3:
            search_value = input("Enter string for searching: ")

        if num_table == 0:
            break
        elif num_table == 1:
            print(list(dict_of_tables.keys())[num_table])
            if num_kind_view == 1:
                for num, record in enumerate(Ich_Edit.get_users(db.cursor)):
                    print(f" {num} - {record}")
        elif num_table == 2:
            print(list(dict_of_tables.keys())[num_table])
            if num_kind_view == 1:
                for num, record in enumerate(Ich_Edit.get_sales(db.cursor)):
                    print(f" {num} - {record}")
        elif num_table == 3:
            print(list(dict_of_tables.keys())[num_table])
            if num_kind_view == 1:
                for num, record in enumerate(Ich_Edit.get_products(db.cursor)):
                    print(f" {num} - {record}")
        print('==' * 15)

        if num_kind_view == 2:
            table_name = list(dict_of_tables.keys())[num_table]
            columns_string = ' | '.join([column for column in Ich_Edit.get_columns(db, table_name)])
            print('-' * len(columns_string))
            print(columns_string)
            print('-' * len(columns_string))

        if num_kind_view == 3:
            table_name = list(dict_of_tables.keys())[num_table]
            result = Ich_Edit.search_all_fields(db, table_name, search_value)
            for value in result:
                print(value)

    db.close()
