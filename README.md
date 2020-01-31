# machine-learning-gen-al
Design is as follows. 

Starting from the bottom up, GenAlModel gives the template for any solution to be solved. A model should have the get_fitness function defined individually, but the GenAlModel class has generic functions for mutate and \_\_lt\_\_ (for sorting).

An Organism holds a single GenAlModel, along with a generation counter. It also defines the get_children function, which handles crossover with a "mate" at a random point in the solution_string. The get_children function will return two children, to reflect both halves of the crossover.   

The Population class holds a list of Organisms, and handles population mechanics. 

Population.\_\_set\_population\_to\_carrying\_capacity will either add random entries up to the carrying capacity, or trim the population to the carrying capacity by eliminating lowest fitness entries.  

Population.\_\_get\_children\_by\_fitness\_tournament has a failsafe if each organism in the population has a fitness of 0, in which case all are flushed and new entries created. Otherwise, the population is mated, with the mate chance being determined by each Organism's fitness divided by the sum of the fitness of the entire population. Mating continues until the carrying capacity is met. 

Population.process\_generation will do a single generation round. This first sets the population to carrying capacity by trimming or random new creation, then creates a new generation using the fitness tournament function above. Each of these new organisms are then mutated. Finally, the top n fitness organisms from the previous generation are added to the new population.

The GenAl and GenAlMulti class are both implementations of the Genetic Algorithm solution. 

The first, GenAl is a simple implementation, just using the Population.process_generation function repeatedly up to generation_max. 

In the GenAlMulti class I have added the concept of islands. In this implementation, I am essentially running multiple GenAl models in parallel. As long as one of the islands has shown some progress, I will allow all of the islands to continue up to "generations", defaulting to 200. When all islands have stalled, a bottleneck is declared, and a clone of the top fitness organism is added to each of the other islands. Processing then restarts. If a further 200 generations are processed without a change in max_fitness, we exit and return the highest fitness organism. 

In theory, this allows us handle local minima by having a crossover of two local minima structures (from competing islands). 

Alternately, if a single entry clearly dominates all others in an island, it will then dominate that population. This allows us to quickly approach an optimal solution, then put more resources into further exploring that near-optimal solution across multiple islands.

I have included several sample solution models. The ExampleSquaredModel is a simple optimization of x^2. 

The KnapsackModel is the problem as described in the assignment. This seemed to be solved with just the original random populations, not really relying on crossover at all.

The KnapsackModelWithNItems is the same problem but allowing more than one repetition of each item, with the mutation function adding or removing a single item each. This did not give reasonably good results.

However, the KnapsackModelExtended is essentially the same problem with a better chance of finding a good solution. The benefit and weight list of the original problem are repeated 64 times (to allow much higher weights). 
ExampleSquaredModel
KnapsackModel
KnapsackModelExtended
KnapsackModelWithNItems

## Output
Sample output for the simple Knapsack model given with the assignment is below:

```
new fitness 7 after 28 steps
new fitness 9 after 1 steps
new fitness 15 after 4 steps
new fitness 17 after 1 steps
new fitness 19 after 32 steps
new fitness 24 after 15 steps
new fitness 27 after 7 steps
Bottleneck! Populations after apex additions:
[27, 27, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[27, 27, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 20, 20, 20, 20, 11, 0, 0]
[27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 24, 0, 0, 0, 0, 0, 0]
[27, 27, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 24, 0, 0, 0, 0, 0, 0]
apex per island at finish:
[27, 27, 27, 27, 27]
after 495 generations
best fitness 27 was generated with generation stamp 294
Found solution 27 
[0, 1, 1, 0, 1, 1, 0]
Time of 0.81
```

Sample output for the KnapsackModelExtended with a weight of 268 is below:
```
new fitness 439 after 4 steps
new fitness 440 after 14 steps
new fitness 441 after 3 steps
new fitness 442 after 3 steps
new fitness 448 after 0 steps
new fitness 449 after 4 steps
new fitness 451 after 5 steps
new fitness 454 after 3 steps
new fitness 457 after 40 steps
new fitness 460 after 53 steps
Bottleneck! Populations after apex additions:
[460, 457, 430, 415, 415, 415, 412, 412, 412, 412, 412, 396, 394, 389, 380, 265, 0, 0, 0, 0]
[460, 457, 430, 430, 430, 430, 430, 430, 418, 416, 415, 409, 394, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[460, 457, 430, 415, 394, 394, 392, 390, 390, 390, 390, 390, 385, 385, 380, 0, 0, 0, 0, 0, 0, 0]
[460, 457, 457, 454, 454, 454, 454, 454, 447, 438, 430, 415, 394, 0, 0, 0, 0, 0, 0, 0]
[460, 460, 460, 460, 460, 460, 460, 460, 457, 456, 430, 415, 394, 351, 257, 0, 0, 0, 0, 0]
new fitness 463 after 184 steps
Bottleneck! Populations after apex additions:
[463, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 458, 0, 0, 0]
[463, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 458, 458, 0, 0, 0, 0]
[463, 463, 463, 463, 463, 463, 463, 463, 463, 461, 460, 460, 460, 460, 0, 0, 0, 0, 0, 0]
[463, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 458, 257, 0, 0, 0, 0, 0]
[463, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 460, 0, 0, 0, 0, 0]
new fitness 466 after 53 steps
Bottleneck! Populations after apex additions:
[466, 466, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 418, 0, 0, 0, 0]
[466, 466, 463, 463, 463, 463, 463, 463, 463, 463, 463, 461, 459, 260, 0, 0, 0, 0, 0, 0]
[466, 466, 466, 466, 466, 466, 466, 466, 466, 466, 466, 466, 463, 463, 463, 0, 0, 0, 0, 0]
[466, 466, 466, 466, 466, 466, 466, 466, 466, 466, 463, 463, 463, 457, 0, 0, 0, 0, 0, 0]
[466, 466, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 463, 0, 0, 0, 0, 0, 0]
apex per island at finish:
[466, 466, 466, 466, 466]
after 1425 generations
best fitness 466 was generated with generation stamp 1224
Found solution 466 
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
Time of 26.11
```

And most interesting, the output for KnapsackModelExtended with a weight of 22 is below.

```
new fitness 32 after 2 steps
new fitness 34 after 0 steps
new fitness 37 after 24 steps
Bottleneck! Populations after apex additions:
[37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 34, 34, 34, 30, 30, 0, 0, 0, 0]
[37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 34, 34, 34, 30, 23, 0, 0, 0, 0, 0]
[37, 37, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 21, 17, 0, 0]
[37, 37, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 25, 25, 23, 21, 21, 18, 0, 0]
[37, 37, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 23, 21, 17, 0, 0]
apex per island at finish:
[37, 37, 37, 37, 37]
after 441 generations
best fitness 37 was generated with generation stamp 12
Found solution 37 
[0, ... 0, 0]
[0, 0, 0, 0, 4, 1, 0]
Time of 6.51
```

