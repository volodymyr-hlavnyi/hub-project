from hw.hw_38.Sale import Sale
from hw.hw_38.User import User
from hw.hw_38.Product import Product


class Ich_Edit:

    @staticmethod
    def get_users(cursor):
        cursor.execute(
            """
            select 
                *
            from users
            ;
            """
        )
        result = cursor.fetchall()
        return [User(data) for data in result]

    @staticmethod
    def get_sales(cursor):
        cursor.execute(
            """
            select 
                *
            from sales
            ;
            """
        )
        result = cursor.fetchall()
        return [Sale(data) for data in result]

    @staticmethod
    def get_products(cursor):
        cursor.execute(
            """
            select 
                *
            from product
            ;
            """
        )
        result = cursor.fetchall()
        return [Product(data) for data in result]

    @staticmethod
    def get_columns(db, table_name):
        db.cursor.execute(
            """
                SELECT COLUMN_NAME 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
                ;
            """, (db.connection.database, table_name))
        result = db.cursor.fetchall()
        return [row[0] for row in result]

    @staticmethod
    def search_all_fields(db, table_name, search_value):
        columns = Ich_Edit.get_columns(db, table_name)
        search_query = f"SELECT * FROM {table_name} WHERE " + " OR ".join([f"{col} LIKE %s" for col in columns])
        search_values = tuple([f"%{search_value}%"] * len(columns))
        db.cursor.execute(search_query, search_values)
        return db.cursor.fetchall()

    @staticmethod
    def search_all_fields_with_eq_sign(db, table_name, search_value_raw):
        columns = Ich_Edit.get_columns(db, table_name)
        search_query = f"SELECT * FROM {table_name} WHERE {str(search_value_raw)};"
        db.cursor.execute(search_query)
        return db.cursor.fetchall()
