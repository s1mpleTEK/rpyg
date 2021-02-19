from Jobs.Soldier import Soldier
from Jobs.Wizzard import Wizzard
from Jobs.Hunter import Hunter

from Races.Dwarf import Dwarf
from Races.Human import Human
from Races.Elf import Elf

JOB = {0:Soldier(), 1:Hunter(), 2: Wizzard()}
RACE = {0:Dwarf(), 1:Human(), 2:Elf()}

class Player:
    def __init__(self):
        self.name = "Bob Debileuh"
        self.job = JOB.get(0)
        # self.money = Money(50)
        self.race = RACE.get(0)
        self.setName()
        self.setRace()
        self.setJob()
    
    def setName(self):
        tmp = input("What's your name ?\n> ")
        print()
        if tmp:
            self.name = tmp

    def setRace(self):
        tmp = input("Choose your race :\n0: Dwarf\n1: Human\n2: Elf\n> ")
        print()
        try:
            tmp = int(tmp)
            if 0<=tmp<=2 and tmp:
                self.race = RACE.get(tmp)
            else:
                return self.setRace()
        except (ValueError, AttributeError):
            if len(tmp) == 0:
                return
            return self.setRace()

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
        print(f"Name: {self.name}")
        self.race.getInfo()
        self.job.getInfo()
        self.job.weapon.getInfo()