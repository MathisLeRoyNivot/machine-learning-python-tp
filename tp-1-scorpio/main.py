import math
import numpy as np
import matplotlib.pyplot as plt

EARTH_GRAVITY_CONST = 9.81
MOON_GRAVITY_CONST = 1.62
JUPITER_GRAVITY_CONST = 24.80
GENERATED_POPULATION_AMOUNT = 20

ROUNDED_ARROW_TYPE = "rounded"
SQUARED_ARROW_TYPE = "squared"


class Arrow:
    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type
    
    @type.setter
    def setType(self, value):
        self._type = value

    def getArrowMass(self):        
        if self._type == ROUNDED_ARROW_TYPE:
            return 
        elif self._type == SQUARED_ARROW_TYPE:
            return


class Material:
    def __init__(self, mass, young_mod, poisson_ratio):
        self._mass = mass
        self._young_mod = young_mod
        self._poisson_ratio = poisson_ratio

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def setMass(self, value):
        self._mass = value

    @property
    def youngMod(self):
        return self._young_mod
    
    @youngMod.setter
    def setYoundMod(self, value):
        self._young_mod = value

    @property
    def poissonRatio(self):
        return self._poisson_ratio
    
    @poissonRatio.setter
    def setPoissonRatio(self, value):
        self._poisson_ratio = value


# ------------------------------------------------------------------------------------------

# Spring constant with Hooke's law
def spring_constant(young_modulus, v):
    if v != 0.5:
        k = (1 / 3) * young_modulus / (1 - 2 * v)
        return k
    return -1


# Empty lenght
def empty_lenght(lb, lc):
    lv = (1 / 2) * (lb**2 - lc**2) ** (1/2)
    return lv


# Move lenght
def move_lenght(lf, lv):
    ld = lf - lv
    return ld
    

# Object mass depending on type
def squared_projectile_mass(density, arrow_base, arrow_height, arrow_lenght):
    mass = density * arrow_base * arrow_height * arrow_lenght
    return mass


def rouded_projectile_mass(density, diameter, arrow_lenght):
    if diameter > 0:
        mass = density * math.pi * (diameter / 2) ** 2 * arrow_lenght
        return mass
    return -1


# Velocity in m.s^-1
def velocity(k, dist, mass):
    if mass > 0:         
        v = (k * dist ** 2 / mass) ** (1/2)
        return v
    return -1


# Range in meters
def range(velocity, g, degree_angle):
    if g != 0 and 0 <= degree_angle < 360:
        radian_angle = math.radians(degree_angle)
        r = (velocity**2 / g) * math.sin(2 * radian_angle)
        return r
    return -1


# KE w/ mass of object in kg and velocity in m.s^-1
def kinetic_energy(mass, velocity):
    ke = (1 / 2) * mass * velocity**2
    return ke


# Equivalence Joule energy
def joule_energy(ke):
    tnt_energy = ke / 4184
    return tnt_energy


# ------------------------------------------------------------------------------------------

materials = {
    'steel': Material(7850, 210, 0.27),
    'aluminum': Material(2700, 62, 0.29),
    'silver': Material(10500, 78, 0),
    'wood': Material(800, 12, 0),
    'bamboo': Material(0, 20, 0),
    'bronze': Material(8740, 110, 0),
    'diamond': Material(3517, 1220, 0),
    'iron': Material(7860, 208, 0.25),
    'or': Material(18900, 78, 0.42),
    'platinum': Material(21450, 170, 0),
    'titanium': Material(4500, 114, 0.34)
}

def generation_population():



def main():
    print("Starting...")
    # plt.scatter(x, y)


if __name__ == "__main__":
    main()
