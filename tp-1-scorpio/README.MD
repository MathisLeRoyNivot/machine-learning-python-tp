# Scorpio Genetic Algorithm

This algorithm determine the best configuration of a scorpio (a medieval weapon) for a launch, depending on the AVAILABLE_MATERIALS, dimensions, etc...

The purpose is to learn the concept of Genetic Algorithm in Machine Learning.

-----
## Presentation

This script calculate a grade for every instance of launch and sort it in a population, to mix the best ranked and make the population evolve.

At the result, we have the best matching specificities for a Scorpio.

-----
## Structure

This script have 4 differents classes:

### Material
![Material Image](assets/material.png)

This class create a material based on its specificities.


### Arrow
![Arrow Image](assets/arrow.png)

This class create an arrow with a material and differents specificities.


### Scorpio
![Scorpio Image](assets/scorpio.png)

This class create a scorpio with an arrow, material and variables properties.


### Launch
![Launch Image](assets/launch.png)

This class create initiate a launch with a scorpio and its arrow. This will be our individual in the population, and its properties will be the genes that will be changed along our algorithm.


-----

## Algorithm functionment

This script execute some steps to determine the best individual for our wanted parameter.

Firstly, one of the main purposes of this algorithm is to determine a *fitness function* that will give a grade for an individual, depending on its results. Nearest it is from the wanted result, bigger will be its fitness.

1 - Generate a random population
2 - Give a grade for every individual (fitness)
3 - Sort population by grades
4 - **Evolve** this population to the next generation
5 - If an individual fitness match the max fitness, then stop algorithm and print the result.

### Fitness

The fitness function will give a grade to an individual based on its distance from the wanted result.

Here, we wanted to have the best configuration to reach a value of cinetic energy at the impact of the arrow.

Our main fitness function will be:
![Fitness Image](assets/fitness.png)

The fitness will vary between 0 and 100, with 100 the maximum, depending on the distance to the wanted energy value. 

### Evolve function

One of the main aspects of the script, with the fitness function, is the evolve function.

It will make the next steps:

1 - Retrieve ordered population by fitness
2 - Select the best ranked individuals
3 - Generate children with 2 random parents genes from the previous individuals choosen
4 - Return new population.

To generate our children, we mix the 2 parents genes. 
To achieve this, there is some methods, but here, we choose to use the Whole Arithmetic Recombination to recalculate random values for the individuals, between the parents ones.


This function will be called while we don't have the solution.

-----
## Usage

To use this script :

```
$ python3 main.py
```
Then, follow the instructions

-----
## Example

Now we make an example to see if our script works.

We want an energy of 450.

For a statistical purpose, we keep an eye on the average fitness of our population, along the evolving.
![Example Image](assets/example_output.png)

And with a graphical representation, here is our results, where we can see the evolving of our population and play with our parameters to use the best ones for our problem.

![Example Graph](assets/bar_chart.svg)