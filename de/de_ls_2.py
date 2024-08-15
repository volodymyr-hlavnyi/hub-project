# Entwickeln Sie eine Funktion sortUsersByBirthday(users), die eine Liste von Benutzern mit ihren Geburtsdaten akzeptiert und diese nach aufsteigendem Alter sortiert.

def sortUsersByBirthday(users):
    return sorted(users, key=lambda user: user.birthday, reverse=True)


if __name__ == '__main__':
    class User:
        def __init__(self, name, birthday):
            self.name = name
            self.birthday = birthday

        def __repr__(self):
            return f"User('{self.name}', '{self.birthday}')"


    users = [
        User('Alice', '1990-01-02'),
        User('Bob', '1990-01-03'),
        User('John', '1990-01-01')
    ]
    # Expected: [User('John', '1990-01-01'), User('Alice', '1990-01-02'), User('Bob', '1990-01-03')]
    for i in users:
        print(i)
    print('-' * 25)
    user_sort = sortUsersByBirthday(users)
    for i in user_sort:
        print(i)
