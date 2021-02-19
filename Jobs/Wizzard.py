from Jobs.Job import Job


import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from Weapons.Magic.Stick import Stick

class Wizzard(Job):
    def __init__(self):
        self.lvl = 1
        self.exp = 0
        self.name = "Wizzard"
        self.weapon = Stick()