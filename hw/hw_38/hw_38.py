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
import re


def get_menu_list():
    menu_1 = [
        'Exit',
        'View Records of table',
        'View list of Column of table',
        'Search value',
        'Search value with < > = <= >=',
    ]

    menu_2 = {
        'Exit': [],
        'users': ['id', 'name', 'age'],
        'sales': ['pid', 'prod', 'quantity'],
        'product': ['sid', 'pid', 'id']
    }

    return menu_1, menu_2


def print_input_menu(menu, _add):
    for number, line in enumerate(menu):
        print(f" {number} - {line}")
    try:
        result = int(input(f'Select {_add} (0 - exit)): '))
    except ValueError as e:
        print(f"Error {e}, please try again...")
        result = print_input_menu(menu, _add)
    return result


def print_content_table(menu, num_table):
    print(list(menu.keys())[num_table])
    if num_table == 1:
        enumerate_object = Ich_Edit.get_users(db.cursor)
    elif num_table == 2:
        enumerate_object = Ich_Edit.get_sales(db.cursor)
    elif num_table == 3:
        enumerate_object = Ich_Edit.get_products(db.cursor)
    for num, record in enumerate(enumerate_object):
        print(f" {num} - {record}")


def print_table_header(menu, num_table):
    table_name = list(menu.keys())[num_table]
    columns_string = ' | '.join([column for column in Ich_Edit.get_columns(db, table_name)])
    print('-' * len(columns_string))
    print(columns_string)
    print('-' * len(columns_string))


def print_search_result(menu, num_table, search_value):
    table_name = list(menu.keys())[num_table]
    result = Ich_Edit.search_all_fields(db, table_name, search_value)
    for value in result:
        print(value)


def print_search_result_with_sign(menu, num_table, search_value):
    table_name = list(menu.keys())[num_table]
    result = Ich_Edit.search_all_fields_with_eq_sign(db, table_name, search_value_raw)
    for value in result:
        print(value)


if __name__ == '__main__':

    db = Connector(get_db_config())

    while True:

        menu_1, menu_2 = get_menu_list()
        print('==' * 15)
        # 1
        num_kind_view = print_input_menu(menu_1, 'type of view')
        if num_kind_view == 0:
            break
        if not num_kind_view in [x for x in range(1, len(menu_1))]:
            print(f"Uncorrected choice, please select from {[x for x in range(0, len(menu_1))]}")
            continue

        # 2
        num_table = print_input_menu(menu_2, 'table')
        if num_table == 0:
            break
        if not num_table in [x for x in range(1, len(menu_2))]:
            print(f"Uncorrected choice, please select from {[x for x in range(0, len(menu_2))]}")
            continue

        # 3
        if num_kind_view == 3:
            search_value = input("Enter string for searching: ")

        # 4
        if num_kind_view == 4:
            table_name = list(menu_2.keys())[num_table]
            columns_list = [column for column in Ich_Edit.get_columns(db, table_name)]
            while True:
                print(columns_list)
                search_value_raw = input("Enter column and < > = <= >= and value (age > 20) : ")
                if search_value_raw.split()[0] in columns_list:
                    break
                else:
                    print(f"First word must be name of column of table, try agan...")

        if num_table in [1, 2, 3] and num_kind_view == 1:
            print_content_table(menu=menu_2, num_table=num_table)

        if num_kind_view == 2:
            print_table_header(menu=menu_2, num_table=num_table)

        if num_kind_view == 3:
            print_search_result(menu=menu_2, num_table=num_table, search_value=search_value)

        if num_kind_view == 4:
            print_search_result_with_sign(menu=menu_2, num_table=num_table, search_value=search_value_raw)

    print("See you soon!")
    db.close()
