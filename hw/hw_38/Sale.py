# Sales с полями (sid, id, pid).
class Sale:
    def __init__(self, data):
        self.sid = data[0]
        self.id = data[1]
        self.pid = data[2]

    def __str__(self):
        return f"sid: {self.sid} | id: {self.id} | pid: {self.pid}"
