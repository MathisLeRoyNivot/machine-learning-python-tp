import math

from Arrow import *
from Scorpio import *


class Launch:
    def __init__(self, scorpio, gravity):
        self.arrow = scorpio.arrow
        self.scorpio = scorpio
        self.gravity = gravity
        self.velocity = self.get_velocity()
        self.reach = self.get_reach()
        self.impact_energy = self.get_impact_energy()

    def get_velocity(self):
        return ((self.scorpio.K * self.scorpio.movement_length ** 2) / self.arrow.mass) ** (1 / 2)

    
    def get_reach(self):
        return (self.velocity ** 2 / self.gravity) * math.sin(2 * (self.scorpio.angle * (math.pi / 180)))

    
    def get_impact_energy(self):
        return 1 / 2 * self.arrow.mass * math.pow(self.velocity, 2)


def get_random_launch(scorpio, gravity):
    return Launch(scorpio, gravity)
