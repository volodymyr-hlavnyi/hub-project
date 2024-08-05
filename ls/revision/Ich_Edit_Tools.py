

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
        return {key: value for key, value in result}