# Course: CS7267
# Student name: Mark Fowler
# Student ID: mfowle19
# Assignment #: #4
# Due Date: November 6, 2019
# Signature:
# Score:

from GenAl import GenAl, GenAlMulti, KnapsackModel, KnapsackModelExtended, KnapsackModelWithNItems
import cProfile
import time
import random

start = time.perf_counter()
myGenAlModel = GenAlMulti(KnapsackModelExtended, generations=200, mutation_chance=0.0001, islands=5, apex_maintenance=5,
                          verbose=True)
found_solution = myGenAlModel.find_solution_with_timeout_and_bottleneck()
print("Found solution %i " % found_solution.get_fitness())
print(found_solution.solution_string)
count = [0, 0, 0, 0, 0, 0, 0]
for x, val in enumerate(found_solution.solution_string):
    if val==1:
        count[x%7]+=1
print(count)
print("Time of %.2f" % (time.perf_counter() - start))

# print("\n\n\n")
#
# start = time.perf_counter()
# myGenAlModel = GenAl(KnapsackModel, generations=1000, mutation_chance=0.0001, apex_maintenance=3)
# found_solution = myGenAlModel.find_solution()
# print("Found solution %i " % found_solution.get_fitness())
# print(found_solution.solution_string)
# print("Time of %.2f" % (time.perf_counter() - start))
#
# print("\n\n\n")
#
# start = time.perf_counter()
# myGenAlModel = GenAlMulti(KnapsackModel, generations=200, mutation_chance=0.0001, islands=5, apex_maintenance=5,
#                           verbose=True)
# found_solution = myGenAlModel.find_solution_with_timeout_and_bottleneck()
# print("Found solution %i " % found_solution.get_fitness())
# print(found_solution.solution_string)
# print("Time of %.2f" % (time.perf_counter() - start))
