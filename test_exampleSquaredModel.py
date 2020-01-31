from unittest import TestCase

from GenAl import ExampleSquaredModel


class TestExampleSquaredModel(TestCase):
    def test_evaluate_solution(self):
        solution_list = [0, 0, 0, 0, 0]
        myModel = ExampleSquaredModel(solution_list)
        self.assertEqual(0, myModel.get_fitness())
        solution_list = [0, 0, 0, 0, 1]
        myModel = ExampleSquaredModel(solution_list)
        self.assertEqual(1, myModel.get_fitness())
        solution_list = [0, 1, 0, 0, 1]
        myModel = ExampleSquaredModel(solution_list)
        self.assertEqual(9, myModel.get_fitness())
        solution_list = [1, 1, 1, 1, 1]
        myModel = ExampleSquaredModel(solution_list)
        self.assertEqual(31, myModel.get_fitness())
