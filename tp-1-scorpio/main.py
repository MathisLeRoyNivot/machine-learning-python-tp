import math
import numpy as np
import random as rd
import matplotlib.pyplot as plt

EARTH_GRAVITY_CONST = 9.81
MOON_GRAVITY_CONST = 1.62
JUPITER_GRAVITY_CONST = 24.80
GENERATED_POPULATION_AMOUNT = 20


class Scorpio:
    def __init__(self, arm_lenght, arm_base, arm_height, string_lenght, young_mod, poisson_ratio, degree_angle, gravity, density, arrow_base, arrow_height, arrow_lenght, arrow):
        self._arm_lenght = arm_lenght
        self._arm_base = arm_base
        self._arm_height = arm_height
        self._string_lenght = string_lenght
        self._young_mod = young_mod
        self._poisson_ratio = poisson_ratio
        self._degree_angle = degree_angle
        self._gravity = gravity
        self._density = density
        self._arrow_lenght = arrow_lenght
        self._arrow_base = arrow_base
        self._arrow_height = arrow_height
        self._fitness = 0

    
    # Spring constant with Hooke's law
    def spring_constant(self, velocity):
        young_modulus = self._young_mod.youngMod()
        if velocity != 0.5:
            k = (1 / 3) * young_modulus / (1 - 2 * velocity)
            return k
        return -1

    
    # Empty lenght
    def empty_lenght(self, lb, lc):
        lv = (1 / 2) * (lb ** 2 - lc ** 2) ** (1/2)
        return lv


    # Move lenght
    def move_lenght(self, lf, lv):
        ld = lf - lv
        return ld


    # Velocity in m.s^-1
    def velocity(self, k, dist, mass):
        if mass > 0:         
            v = (k * dist ** 2 / mass) ** (1/2)
            return v
        return -1


    # Range in meters
    def scorpio_range(self, velocity, g, degree_angle):
        if g != 0 and 0 <= degree_angle <= 90:
            radian_angle = math.radians(degree_angle)
            r = (velocity ** 2 / g) * math.sin(2 * radian_angle)
            return r
        return -1

    
    # KE w/ mass of object in kg and velocity in m.s^-1
    def kinetic_energy(self, mass, velocity):
        ke = (1 / 2) * mass * velocity ** 2
        return ke


    # Equivalence Joule energy
    def joule_energy(self, ke):
        tnt_energy = ke / 4184
        return tnt_energy


ROUNDED_ARROW_TYPE = "rounded"
SQUARED_ARROW_TYPE = "squared"


class Arrow:
    def __init__(self, type, density, arrow_base, arrow_height, arrow_lenght, diameter):
        self._type = type
        self._density = density
        self._arrow_base = arrow_base
        self._arrow_height = arrow_height
        self._arrow_lenght = arrow_lenght
        self._diameter = diameter

    @property
    def type(self):
        return self._type
    

    @type.setter
    def setType(self, value):
        self._type = value


    def getArrowMass(self):        
        if self._type == ROUNDED_ARROW_TYPE :
            return self.squared_projectile_mass()
        elif self._type == SQUARED_ARROW_TYPE and self._diameter > 0:
            return self.rouded_projectile_mass()


    # Object mass depending on type
    def squared_projectile_mass(self):
        mass = self._density * self._arrow_base * self._arrow_height * self._arrow_lenght
        return mass


    def rouded_projectile_mass(self):
        if self._diameter > 0:
            mass = self._density * math.pi * (self._diameter / 2) ** 2 * self._arrow_lenght
            return mass
        return -1


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
AVAILABLE_MATERIALS = {
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

populations = []

def generate_population():
    print("Generating populations...")
    for i in range(GENERATED_POPULATION_AMOUNT):
        Materiau = rd.choice(AVAILABLE_MATERIALS)
        populations.append(
            Scorpio(rd.randrange(0, 100, 1), rd.randrange(0, 100, 1), Materiau.module_young,
                                   Materiau.coef_poisson, rd.randrange(0, 90, 1), 9.81, Materiau.masse_volumique, rd.randrange(0, 100, 1)/100, rd.randrange(0, 100, 1)/100, rd.randrange(0, 100, 1), rd.randrange(0, 100, 1), rd.randrange(0, 100, 1))
            )


def set_fitnesses():
    for population in populations:
        if(population.is_tir() == True):
            population.fitness = population.energie_impact() * population.scorpio_range() * 2
        else:
            population.fitness = 0


def selection():
    populations.sort(key=lambda x: x.fitness, reverse=True)
    for x in range(round(GENERATED_POPULATION_AMOUNT / 2), GENERATED_POPULATION_AMOUNT - 1):
        del populations[round(GENERATED_POPULATION_AMOUNT / 2)]


def croisements():
    probs = [i.fitness for i in populations]
    probs /= np.sum(probs)
    nouvelle_population = []
    for pop in populations:
        scorpion2 = np.random.choice(populations, p=probs)
        bebe_scorpion = croisement(pop, scorpion2)
        nouvelle_population.append(bebe_scorpion)
        while True:
            scorpion3 = np.random.choice(populations, p=probs)
            if(scorpion3.fitness != scorpion2.fitness):
                bebe_scorpion2 = croisement(pop, scorpion3)
                if(bebe_scorpion2 not in nouvelle_population):
                    nouvelle_population.append(bebe_scorpion2)
                    break

    return nouvelle_population


def croisement(scorpio1, scorpio2):
    return Scorpio(scorpio1.longueur_bras, scorpio1.longueur_corde, scorpio1.module_young, scorpio1.coef_poisson, scorpio1.angle_deg, scorpio1.gravite, scorpio1.masse_volumique, scorpio2.base_fleche, scorpio2.hauteur_fleche, scorpio2.longueur_fleche, scorpio2.base_bras, scorpio2.hauteur_bras)


def mutations():
    for i in range(0, len(populations)-1):
        if(decision(0.5)):
            populations[i].longueur_corde += 1


def afficher_population(i):
    print(f'POPULATION #{i}: {avg_fitness()} / {max_fitness()}')
    # for pop in populations:
    # print(pop.fitness)


def decision(probability):
    return rd.random() < probability


def max_fitness():
    fitnesses = [i.fitness for i in populations]
    return np.amax(fitnesses)


def avg_fitness():
    fitnesses = [i.fitness for i in populations]
    return np.mean(fitnesses)


def main():
    print("🟢 Starting...")
    # plt.scatter(x, y)

    print("🔴 Program ended")


if __name__ == "__main__":
    main()
