import unittest
from classes.WaterBottleProblem import WaterBottleProblem
from classes.Node import Node
from classes.Bottle import Bottle

# This is a test class for the WaterBottleProblem class
class WaterBottleProblemTest(unittest.TestCase):
    def test_init(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        self.assertEqual(problem.initial, initial)
        self.assertEqual(problem.goal, goal)

    def test_repr(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        self.assertEqual(str(problem), f"<WaterBottleProblem <Node {b1,b2,b3}>>")

    def test_actions(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        actions = problem.actions(initial.state)
        self.assertEqual(len(actions), 5)
        self.assertIn(("fill", b2), actions)
        self.assertIn(("fill", b3), actions)
        self.assertIn(("empty", b1), actions)
        self.assertIn(("pour", b1, b2), actions)
        self.assertIn(("pour", b1, b3), actions)

    def test_result(self):
        b_1 = Bottle(10)
        b_1.current = 10
        b_2 = Bottle(6)
        b_2.current = 0
        b_3 = Bottle(5)
        b_3.current = 0
        initial = Node((b_1, b_2, b_3))

        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        b1 = Bottle(10)
        b1.current = 0
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        expected = Node((b1, b2, b3))
        self.assertEqual(problem.result(initial.state, ("empty", b_1)), expected.state)


    def test_h(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        self.assertEqual(problem.h(initial.state), 20)

    def test_goal_test(self):
        b1 = Bottle(10)
        b1.current = 0
        b2 = Bottle(6)
        b2.current = 5
        b3 = Bottle(5)
        b3.current = 5
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        self.assertTrue(problem.goal_test(initial))
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 1
        initial = Node((b1, b2, b3))
        self.assertFalse(problem.goal_test(initial))

    def test_path_cost(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        self.assertEqual(problem.path_cost(0, initial.state, "fill", initial.state), 1)

    def test_value(self):
        b1 = Bottle(10)
        b1.current = 10
        b2 = Bottle(6)
        b2.current = 0
        b3 = Bottle(5)
        b3.current = 0
        initial = Node((b1, b2, b3))
        goal = (0, 5, 5)
        problem = WaterBottleProblem(initial, goal)
        with self.assertRaises(NotImplementedError):
            problem.value()

if __name__ == "__main__":
    unittest.main()