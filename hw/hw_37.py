# Python: домашние задание 37 morning (Python)
#
# В базе данных ich_edit три таблицы.
# Users с полями (id, name, age), Products с полями
# (pid, prod, quantity) и Sales с полями (sid, id, pid).
#
# Программа должна запросить у пользователя
# название таблицы и вывести все ее строки или сообщение,
# что такой таблицы нет.
#
# В базе данных ich_edit три таблицы.
# Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и
# Sales с полями (sid, id, pid).
#
# Программа должна вывести все имена из таблицы users,
# дать пользователю выбрать одно из них и
# вывести все покупки этого пользователя.

# select * from Users;
# select * from Sales;
# SELECT * from Products;

import mysql.connector


def get_list_of_all_tables():
    cursor, connection = get_connect()
    cursor.execute("""
    SELECT
        TABLE_NAME
    FROM
        information_schema.tables
    WHERE
        table_schema = 'ich_edit';
    """)
    return list(cursor.fetchall())


def get_table_name():
    get_connect()
    str_of_tables = ', '.join(tab[0] for tab in get_list_of_all_tables())
    print(f"List of existed tables: ({str_of_tables})")
    table_name = input("Enter table name: ")
    return table_name


def get_user_id():
    user_id_str = input("Enter user id: ")
    user_id = int(user_id_str) if user_id_str.isdigit() else 1
    return user_id


class Connector:
    def __init__(self, config):
        print("Opening connection...")
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        print("Connection established")

    def __del__(self):
        print("Closing connection...")
        self.cursor.close()
        self.connection.close()
        print("Connection closed")


def get_connect(database='ich_edit'):
    dbconfig = {
        'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
        'user': 'ich1',
        'password': 'password',
        'database': database,
    }

    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    return cursor, connection


def close_connect(cursor, connection):
    cursor.close()
    connection.close()


def get_table(cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        result = None
    return result


def get_user_purchases(cursor, t_user, t_prod, t_sales, user_id):
    cursor.execute(
        f"""
        SELECT 
	        * 
        from {t_user} as u
        join {t_sales} as s 
	        on u.id = s.id
        join {t_prod} as p
	        on s.pid = p.pid
	    WHERE u.id = {user_id}
	"""
    )
    result = cursor.fetchall()
    return result


def main():
    table_name = get_table_name()
    cursor, connection = get_connect()
    table = get_table(cursor, table_name)
    if table:
        for row in table:
            print(row)
    else:
        print(f"Table {table_name} does not exist")
    close_connect(cursor, connection)

    print("- Users: -")
    print("1 - Users")
    print("2 - users")
    input_table_users_name = input("Enter number witch table you want to see: ")
    try:
        table_name_4_users = 'Users' if input_table_users_name == '1' else 'users'
    except:
        print("Wrong table number, using default table 'Users'")
        table_name_4_users = 'Users'
    cursor, connection = get_connect()
    table = get_table(cursor, table_name_4_users)
    for user in table:
        print(user)
    user_id = get_user_id()
    cursor, connection = get_connect()
    table_name_4_sales = 'Sales' if table_name_4_users == 'Users' else 'sales'
    table_name_4_prod = 'Products' if table_name_4_users == 'Users' else 'product'
    user_purchases = get_user_purchases(
        cursor,
        table_name_4_users,
        table_name_4_prod,
        table_name_4_sales,
        user_id)
    if user_purchases:
        if len(user_purchases) == 0:
            print(f"User {user_id} has no purchases")
        for row in user_purchases:
            print(row[-3], row[-2], row[-1])
    else:
        print(f"User {user_id} does not exist")
    close_connect(cursor, connection)


if __name__ == '__main__':
    main()
