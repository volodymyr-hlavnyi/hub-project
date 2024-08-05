# pip install mysql-connector-python

import mysql.connector


class Connector:
    def __init__(self, config):
        print("Opening connection...")
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        print("Connection established")

    def close(self):
        print("Closing connection...")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
