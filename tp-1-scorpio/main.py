from prettytable import PrettyTable
from random import randrange, uniform, random, choice

from Arrow import *
from Launch import *
from Material import *
from Scorpio import *

EARTH_GRAVITY_CONST = 9.81
MOON_GRAVITY_CONST = 1.62
JUPITER_GRAVITY_CONST = 24.80

PROBABILITY_TO_MUTATE = 0.1
PROBABILITY_TO_KEEP_GRATED = 0.2
PROBABILITY_TO_KEEP_NON_GRATED = 0.05
POPULATION_AMOUNT = 500
GENERATION_MAX_AMOUNT = 100
FITNESS_MAX = 100

EXPECTED_ENERGY = input('Energy in joules you want to reach: ')
BEST_GRADED_PERCENTAGE = int(POPULATION_AMOUNT * PROBABILITY_TO_KEEP_GRATED)


# Get Random population
def generate_random_population():
    return [get_random_launch(get_random_scorpio(get_random_arrow()), EARTH_GRAVITY_CONST) for _ in
            range(POPULATION_AMOUNT)]


# Get Individual Fitness
def get_fitness(launch):
    fitness = 100 / (abs(float(EXPECTED_ENERGY) - float(launch.impact_energy)) + 1)
    return fitness


# Get average Fitness
def get_average_fitness(population):
    totalFitness = 0
    for launch in population:
        totalFitness += get_fitness(launch)
    return totalFitness / POPULATION_AMOUNT


# Sort population
def rank_population(population):
    ranked_population = []
    for launch in population:
        ranked_population.append((launch, get_fitness(launch)))
    return sorted(ranked_population, key=lambda x: x[1], reverse=True)


# Make population evolve for 1 generation
def evolve_population(population):
    # Retrieve ranked Population
    sorted_population = rank_population(population)
    average_fitness = 0
    solution = []
    ranked_population = []

    # Give grade and get average grade
    for launch, fitness in sorted_population:
        average_fitness += fitness
        ranked_population.append(launch)
        if fitness >= (FITNESS_MAX - 0.01):  # Child will be near to perfect FITNESS_MAX but never equal
            solution.append(launch)
    average_fitness /= POPULATION_AMOUNT

    # End the script when solution is found
    if solution:
        return population, average_fitness, solution

    # Keep Best ranked launches
    parents = ranked_population[:BEST_GRADED_PERCENTAGE]

    # Add some random launches
    for launch in ranked_population[BEST_GRADED_PERCENTAGE:]:
        if random() < PROBABILITY_TO_KEEP_NON_GRATED:
            parents.append(launch)

    # Random mutation in population
    for launch in parents:
        if random() < PROBABILITY_TO_MUTATE:
            launch = get_random_launch(get_random_scorpio(get_random_arrow()), EARTH_GRAVITY_CONST)

    # Crossover
    wanted_length = POPULATION_AMOUNT - len(parents)
    children = []
    while len(children) < wanted_length:
        parent_scorpio_1 = choice(parents)
        parent_scorpio_2 = choice(parents)

        # Create new Arrow
        child_arrow = Arrow(
            parent_scorpio_1.scorpio.arrow.material,
            round(uniform(parent_scorpio_1.scorpio.arrow.length, parent_scorpio_2.scorpio.arrow.length),
                  arrow_data['length']['precision']),
            round(uniform(parent_scorpio_1.scorpio.arrow.diameter, parent_scorpio_2.scorpio.arrow.diameter),
                  arrow_data['diameter']['precision'])
        )

        # Create new Scorpio
        child_scorpio = Scorpio(
            child_arrow,
            parent_scorpio_2.scorpio.material,
            round(uniform(parent_scorpio_1.scorpio.arm_length, parent_scorpio_2.scorpio.arm_length),
                  scorpio_data['arm_length']['precision']),
            round(uniform(parent_scorpio_1.scorpio.arm_base, parent_scorpio_2.scorpio.arm_base),
                  scorpio_data['arm_base']['precision']),
            round(uniform(parent_scorpio_1.scorpio.arm_height, parent_scorpio_2.scorpio.arm_height),
                  scorpio_data['arm_height']['precision']),
            round(uniform(parent_scorpio_1.scorpio.string_length, parent_scorpio_2.scorpio.string_length),
                  scorpio_data['string_length']['precision']),
            round(uniform(parent_scorpio_1.scorpio.angle, parent_scorpio_2.scorpio.angle), scorpio_data['angle']['precision'])
        )

        # Create new Launch
        child_launch = Launch(
            child_scorpio,
            EARTH_GRAVITY_CONST
        )

        child = child_launch
        children.append(child)

    parents.extend(children)
    return parents, average_fitness, solution


# Main program
def main():
    population = generate_random_population()  # Generate initial population
    average_fitness = get_average_fitness(population)  # Give grades to population

    # Evolve
    i = 0
    solution = None
    average_fitness_log = []
    while not solution and i < GENERATION_MAX_AMOUNT:
        population, average_fitness, solution = evolve_population(population)
        print(f'Generation {i} has a fitness of: {round(average_fitness / FITNESS_MAX * 100, 2)}%')
        average_fitness_log.append(round(average_fitness, 2))
        i += 1

    print(f'Final average fitness: {round(average_fitness / FITNESS_MAX * 100, 2)}%')  # Print the final stats

    # Print the solution
    if solution:
        x = PrettyTable()
        y = PrettyTable()

        print(f'Ideal Scorpio found after {i} generations with a fitness : {get_fitness(solution[0])}%.')
        print('Ideal Scorpio: ')
        x.field_names = ["Property", "Value"]
        x.add_row(["Material", str(solution[0].scorpio.material.name)])
        x.add_row(["Arm length", str(solution[0].scorpio.arm_length)])
        x.add_row(["Arm base", str(solution[0].scorpio.arm_base)])
        x.add_row(["Arm height", str(solution[0].scorpio.arm_height)])
        x.add_row(["String length", str(solution[0].scorpio.string_length)])
        x.add_row(["Shoot angle", str(solution[0].scorpio.angle)])
        print(x)

        print('Ideal Arrow: ')
        y.field_names = x.field_names
        y.add_row(["Material", str(solution[0].arrow.material.name)])
        y.add_row(["Length", str(solution[0].arrow.length)])
        y.add_row(["Diameter", str(solution[0].arrow.diameter)])
        print(y)
    else:
        print(f'No solution found after {i} generations.')
        print('- Last population was:')
        for number, launch in enumerate(population):
            print(number, '->', ''.join(launch))


if __name__ == '__main__':
    main()
