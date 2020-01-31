# Course: CS7267
# Student name: Mark Fowler
# Student ID: mfowle19
# Assignment #: #4
# Due Date: November 6, 2019
# Signature:
# Score:

from unittest import TestCase
from GenAl import ExampleSquaredModel, GenAl, KnapsackModel,GenAlMulti
import random

class TestGenAl(TestCase):
    # def test___create_population(self):
    #     myGenAlModel = GenAl(ExampleSquaredModel)
    #     self.assertEqual(10, myGenAlModel.carrying_capacity)
    #     # for model in myGenAlModel.population:
    #     #     print(model.get_fitness())

    def test_find_solution(self):
        random.seed(1)
        myGenAlModel = GenAl(ExampleSquaredModel)
        # self.assertEqual(10, myGenAlModel.carrying_capacity)
        found_solution = myGenAlModel.find_solution()
        print(found_solution.get_fitness())
        print(found_solution.solution_string)

    def test_find_solution2(self):
        # for x in range(20):
        #     random.seed(x)
            myGenAlModel = GenAl(KnapsackModel)
            # self.assertEqual(10, myGenAlModel.carrying_capacity)
            found_solution = myGenAlModel.find_solution()
            print(found_solution.get_fitness())

            print(found_solution.solution_string)

    def test_find_solution3(self):

        myGenAlModel = GenAlMulti(KnapsackModel,generations=200)
        # myGenAlModel = GenAlMulti(KnapsackModel)
        found_solution = myGenAlModel.find_solution()
        print(found_solution.get_fitness())
        print(found_solution.solution_string)

    def test_find_solution_with_timeout(self):
        for x in range(20):
            random.seed(x)
            myGenAlModel = GenAlMulti(KnapsackModel,generations=200,mutation_chance=0.01,islands=5)
            # myGenAlModel = GenAlMulti(KnapsackModel)
            found_solution = myGenAlModel.find_solution_with_timeout()
            print("Found solution %i"%found_solution.get_fitness())
            print(len(found_solution.solution_string))
            print(found_solution.solution_string)

    def test_find_solution_with_timeout_and_bottleneck(self):
        # for x in range(1):
        #     x=4
        #     random.seed(x)
            myGenAlModel = GenAlMulti(KnapsackModel,generations=200,mutation_chance=0.0001,islands=5)
            # myGenAlModel = GenAlMulti(KnapsackModel)
            found_solution = myGenAlModel.find_solution_with_timeout_and_bottleneck()
            print("Found solution %i"%found_solution.get_fitness())
            print(len(found_solution.solution_string))
            print(found_solution.solution_string)

