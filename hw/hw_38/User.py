class User:
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.age = data[2]

    def __str__(self):
        return f"Name: {self.name} age: {self.age}"
