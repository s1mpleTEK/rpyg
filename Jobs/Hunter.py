from Jobs.Job import Job

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from Weapons.Distance.Bow import Bow

class Hunter(Job):
    def __init__(self):
        self.lvl = 1
        self.name = "Hunter"
        self.exp = 0
        self.weapon = Bow()