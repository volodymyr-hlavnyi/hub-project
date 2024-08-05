from hw.hw_37 import Connector

#
# ich_edit три таблицы.
# Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и
# Sales с полями (sid, id, pid).
dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'ich_edit',
}

db = Connector(dbconfig)


def get_table(table_name):
    tables = {
        'Users': ('id', 'name', 'age'),
        'Products': ('pid', 'prod', 'quantity'),
        'Sales': ('sid', 'id', 'pid')}
    if table_name in tables:
        return tables[table_name]
    else:
        return None


def get_list_of_all_tables():
    db.cursor.execute(
        """
    SELECT
        TABLE_NAME
    FROM
        information_schema.tables
    WHERE
        table_schema = 'ich_edit';
    """)
    return list(db.cursor.fetchall())


def input_table_name():
    table_name = input("Enter table name: ")
    return table_name


if __name__ == '__main__':

    table_name = input_table_name()
    table = get_table(table_name)
    if table:
        print(f"Table {table_name} found, fields: {table}")
    else:
        print("Table not found")
