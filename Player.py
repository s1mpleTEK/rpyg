from Class.Soldier import Soldier
from Class.Wizzard import Wizzard
from Class.Hunter import Hunter

JOB = {0:Soldier, 1:Hunter, 2: Wizzard}

class Player:
    def __init__(self):
        self.name = "Bob Debileuh"
        self.job = JOB.get(0)
        # self.money = Money(50)
        # self.race = Dwarf()
    
    def setName(self):
        tmp = input("What's your name ?\n> ")
        print()
        if tmp:
            self.name = tmp

    def setJob(self):
        tmp = input("Choose your job now:\n0: Soldier\n1: Hunter\n2: Wizzard\n> ")
        print()
        try:
            tmp = int(tmp)
            if 0<=tmp<=2 and tmp:
                self.job = JOB.get(tmp)
            else:
                return self.setJob()
        except (ValueError, AttributeError):
            if len(tmp) == 0:
                return
            return self.setJob()

    def getInfo(self):
        print(f"name = {self.name}\njob = {self.job().getName()}")