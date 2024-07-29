# pip install mysql-connector-python

import mysql.connector


def ls49_get_connect():
    dbconfig = {
        'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
        'user': 'ich1',
        'password': 'password',
        'database': 'ich_edit'
    }

    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    return cursor, connection


def ls49_close_connect(cursor, connection):
    cursor.close()
    connection.close()


def ls49_1(cursor):
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)




def ls49_2(cursor, connection):
    name = "Franklin"
    age = 45
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))

    # data = {"name": "John", "age": 25}
    # cursor.execute("INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)", data)
    connection.commit()


def ls49_3(cursor, connection):
    data = [("Esel", 15), ("Shrek", 40), ("Fiona", 28)]
    cursor.executemany("INSERT INTO users (name, age) VALUES (%s, %s)", data)
    connection.commit()


def ls49_4_transact(cursor, connection):
    try:
        connection = mysql.connector.connect(**dbconfig)
        cursor = connection.cursor()
        # Выполнение операций в рамках транзакции
        connection.commit()
    except:
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    try:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 25))
        connection.commit()
    except mysql.connector.Error as e:
        print("Ошибка базы данных:", e)
        connection.rollback()

def ls49_11(cursor, age):
    cursor.execute("SELECT * FROM users WHERE age > %s", (age,))
    result = cursor.fetchall()
    for row in result:
        print(row)

# В базе данных ich_edit три таблицы.
# Users с полями (id, name, age),
# Product с полями (pid, prod, quantity) и
# Sales с полями (sid, id, pid).
# Программа должна вывести все покупки каждого пользователя.
def ls49_12(cursor):
    cursor.execute(
        """
           select *
        from
	        users as u
        join sales as s
	on  
	u.id = s.id
join product as p
	on s.pid = p.pid
	;
	"""
    )
    result = cursor.fetchall()
    for row in result:
        print(f"user: {row[1]} product: {row[-2]} quantity: {row[-1]}")



if __name__ == '__main__':
    curs, conn = ls49_get_connect()
    # ls49_1(curs)
    # ls49_2(curs, conn)
    # ls49_3(curs, conn)
    # ls49_4_transact(curs, conn)
    # ls49_close_connect(curs, conn)
    # age = input('Enter age: ')
    # ls49_11(curs, int(age))
    ls49_12(curs)

