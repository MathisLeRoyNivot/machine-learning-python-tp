import math
import random as rd
from Material import *


arrow_data = {
    'length': {
        'min': 0.6,
        'max': 0.8,
        'precision': 3
    },
    'diameter': {
        'min': 0.005,
        'max': 0.03,
        'precision': 3
    }
}

class Arrow:
    def __init__(self, material, length, diameter):
        self.material = material
        self.length = length
        self.diameter = diameter
        self.mass = self.get_mass()

    def get_mass(self):
        return self.material.mass * (math.pi * (self.diameter / 2) ** 2) * self.length


def get_random_arrow():
    return Arrow(
        AVAILABLE_MATERIALS[rd.randrange(0, len(AVAILABLE_MATERIALS))],
        round(rd.uniform(arrow_data['length']['min'], arrow_data['length']['max']), arrow_data['length']['precision']),
        round(rd.uniform(arrow_data['diameter']['min'], arrow_data['diameter']['max']), arrow_data['diameter']['precision']),
    )