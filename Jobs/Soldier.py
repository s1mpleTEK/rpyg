from Jobs.Job import Job

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from Weapons.Melee.Sword import Sword

class Soldier(Job):
    def __init__(self):
        self.lvl = 1
        self.name = "Soldier"
        self.exp = 0
        self.weapon = Sword()