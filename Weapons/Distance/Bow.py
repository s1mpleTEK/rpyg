import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from Weapons.Weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        self.name = "Bow"
        self.power = 100