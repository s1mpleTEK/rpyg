import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from Weapons.Melee.Arms import Arms

class Job:
    def __init__(self):
        self.lvl = 0
        self.name = ""
        self.exp = 0
        self.weapon = Arms()

    def getName(self):
        return self.name

    def setExp(self, exp):
        self.exp += exp

    def getExp(self):
        return self.exp

    def getInfo(self):
        print(f"Class:\n\tName: {self.name}\n\tLvl: {self.lvl}\n\tExp: {self.exp}")