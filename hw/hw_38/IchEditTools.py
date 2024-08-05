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
            from Users
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
            from Sales
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
            from Products
            ;
            """
        )
        result = cursor.fetchall()
        return [Product(data) for data in result]
