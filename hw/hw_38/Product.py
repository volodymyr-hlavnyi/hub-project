# Products с полями (pid, prod, quantity)
class Product:
    def __init__(self, data):
        self.pid = data[0]
        self.prod = data[1]
        self.quantity = data[2]

    def __str__(self):
        return f"pid: {self.prod} prod: {self.prod} quantity: {self.quantity}"
