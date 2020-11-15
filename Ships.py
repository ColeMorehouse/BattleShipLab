class ships:

    def __init__(self, t, d):
        self.type = t
        self.direction = d
        lengths = {
            "D": 2,
            "S": 3,
            "C": 3,
            "B": 4,
            "A": 5
        }
        self.length = lengths[t]

    def getLength(self):
        return self.length

    def getType(self):
        return self.type

    def getDirection(self):
        return self.direction