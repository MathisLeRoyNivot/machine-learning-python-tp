import math
import random as rd

from Arrow import *
from Material import *

scorpio_data = {
    'arm_length': {
        'min': 4,
        'max': 6,
        'precision': 3
    },
    'arm_base': {
        'min': 0.03,
        'max': 0.2,
        'precision': 3
    },
    'arm_height': {
        'min': 0.03,
        'max': 0.2,
        'precision': 3
    },
    'string_length': {
        'min': 1.5,
        'max': 4,
        'precision': 3
    },
    'angle': {
        'min': 0,
        'max': 90,
        'precision': 1
    }
}


class Scorpio:
    def __init__(self, arrow, material, arm_length, arm_base, arm_height, string_length, angle):
        self.arrow = arrow
        self.material = material
        self.arm_length = arm_length
        self.arm_base = arm_base
        self.arm_height = arm_height
        self.string_length = string_length
        self.angle = angle

        self.empty_length = (1 / 2) * math.sqrt(self.arm_length ** 2 - self.string_length ** 2) ** (1/2)
        self.movement_length = arrow.length - self.empty_length
        self.I = (self.arm_base * math.pow(self.arm_height, 3)) / 12

        self.K = (1 / 3) * (material.young_mod / (1 - (2 * material.poisson_ratio)))
        self.F = self.K * self.movement_length
        self.force = (self.F * self.arm_length ** 3) / (48 * material.young_mod * self.I)


def get_random_scorpio(arrow):
    return Scorpio(
        arrow,
        AVAILABLE_MATERIALS[rd.randrange(0, len(AVAILABLE_MATERIALS))],
        round(rd.uniform(scorpio_data['arm_length']['min'], scorpio_data['arm_length']['max']),
              scorpio_data['arm_length']['precision']),
        round(rd.uniform(scorpio_data['arm_base']['min'], scorpio_data['arm_base']['max']), scorpio_data['arm_base']['precision']),
        round(rd.uniform(scorpio_data['arm_height']['min'], scorpio_data['arm_height']['max']),
              scorpio_data['arm_height']['precision']),
        round(rd.uniform(scorpio_data['string_length']['min'], scorpio_data['string_length']['max']),
              scorpio_data['string_length']['precision']),
        round(rd.uniform(scorpio_data['angle']['min'], scorpio_data['angle']['max']), scorpio_data['angle']['precision']),
    )