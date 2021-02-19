class Weapon:
    def __init__(self):
        self.name = ""
        self.power = 0

    def getInfo(self):
        print(f"Weapon:\n\tName: {self.name}\n\tPower: {self.power}")