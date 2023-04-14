import unittest
from classes.WaterBottleProblem import *

# Write a test class that inherits from unittest.TestCase
# Test the following methods of the WaterBottleProblem class:
#   > __init__
#   > __repr__
#   > actions
#   > result
#   > h
#   > goal_test
#   > path_cost
class WaterBottleProblemTest(unittest.TestCase):
    def test_init(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(water_bottles.b1.capacity, 5)
        self.assertEqual(water_bottles.b2.capacity, 3)

    def test_repr(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(repr(water_bottles), "WaterBottleProblem(b1=Bottle(capacity=5, current=0), b2=Bottle(capacity=3, current=0))")

    def test_actions(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(water_bottles.actions(water_bottles), ['Fill 5L', 'Fill 3L', 'Empty 5L', 'Empty 3L', 'Pour 5L into 3L', 'Pour 3L into 5L'])

    def test_result(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(water_bottles.result(water_bottles, 'Fill 5L'), WaterBottleProblem(5, 0))
        self.assertEqual(water_bottles.result(water_bottles, 'Fill 3L'), WaterBottleProblem(0, 3))
        self.assertEqual(water_bottles.result(water_bottles, 'Empty 5L'), WaterBottleProblem(0, 0))
        self.assertEqual(water_bottles.result(water_bottles, 'Empty 3L'), WaterBottleProblem(0, 0))
        self.assertEqual(water_bottles.result(water_bottles, 'Pour 5L into 3L'), WaterBottleProblem(2, 3))
        self.assertEqual(water_bottles.result(water_bottles, 'Pour 3L into 5L'), WaterBottleProblem(5, 0))

    def test_h(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(water_bottles.h(water_bottles), 0)

    def test_goal_test(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertFalse(water_bottles.goal_test(water_bottles))
        water_bottles.b1.fill(5)
        self.assertFalse(water_bottles.goal_test(water_bottles))
        water_bottles.b2.fill(3)
        self.assertTrue(water_bottles.goal_test(water_bottles))

    def test_path_cost(self):
        water_bottles = WaterBottleProblem(5, 3)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Fill 5L', water_bottles), 1)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Fill 3L', water_bottles), 1)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Empty 5L', water_bottles), 1)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Empty 3L', water_bottles), 1)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Pour 5L into 3L', water_bottles), 1)
        self.assertEqual(water_bottles.path_cost(0, water_bottles, 'Pour 3L into 5L', water_bottles), 1)

if __name__ == '__main__':
    unittest.main()