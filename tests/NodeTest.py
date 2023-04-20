import unittest
from classes.Node import *
from classes.Problem import *

# Write a test class that inherits from unittest.TestCase
class NodeTest(unittest.TestCase):
    def test_init(self):
        node = Node(1)
        self.assertEqual(node.state, 1)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.action, None)
        self.assertEqual(node.path_cost, 0)
        self.assertEqual(node.depth, 0)

    def test_repr(self):
        b1 = Bottle(8)
        b2 = Bottle(5)
        b3 = Bottle(3)
        state = Node(b1, b2, b3)
        self.assertEqual(repr(state), "<Node(Bottle(8), Bottle(5), Bottle(3))>")

    def test_expand(self):
        node = Node((Bottle(8), Bottle(5), Bottle(3)))
        problem = WaterBottleProblem(node)
        self.assertEqual(len(node.expand(problem)), 2)
        self.assertEqual(node.expand(problem)[0].state, Bottle(8, 8))
        self.assertEqual(node.expand(problem)[1].state, Bottle(0, 5))

    def test_path(self):
        b1 = Bottle(8)
        b2 = Bottle(5)
        b3 = Bottle(3)
        node = Node(b1, b2, b3)
        self.assertEqual(node.path(), [node])

        b1 = Bottle(8, 8)
        b2 = Bottle(5, 0)
        b3 = Bottle(3, 0)
        node = Node(b1, b2, b3, parent=node)
        self.assertEqual(node.path(), [node.parent, node])

        b1 = Bottle(8, 8)
        b2 = Bottle(5, 0)
        b3 = Bottle(3, 3)
        node = Node(b1, b2, b3, parent=node)
        self.assertEqual(node.path(), [node.parent.parent, node.parent, node])

    def test_solution(self):
        b1 = Bottle(8)
        b2 = Bottle(5)
        b3 = Bottle(3)
        node = Node(b1, b2, b3)
        self.assertEqual(node.solution(), [])

        b1 = Bottle(8, 8)
        b2 = Bottle(5, 0)
        b3 = Bottle(3, 0)
        node = Node(b1, b2, b3, parent=node)
        self.assertEqual(node.solution(), ["Fill bottle 1"])

        b1 = Bottle(8, 8)
        b2 = Bottle(5, 0)
        b3 = Bottle(3, 3)
        node = Node(b1, b2, b3, parent=node)
        self.assertEqual(node.solution(), ["Fill bottle 1", "Pour bottle 1 into bottle 3"])

    def test_queue_frontier(self):
        frontier = QueueFrontier()
        self.assertEqual(frontier.empty(), True)
        self.assertEqual(frontier.contains_state(1), False)
        node = Node(1)
        frontier.add(node)
        self.assertEqual(frontier.empty(), False)
        self.assertEqual(frontier.contains_state(1), True)
        self.assertEqual(frontier.remove(), node)

    def test_stack_frontier(self):
        frontier = StackFrontier()
        self.assertEqual(frontier.empty(), True)
        self.assertEqual(frontier.contains_state(1), False)
        node = Node(1)
        frontier.add(node)
        self.assertEqual(frontier.empty(), False)
        self.assertEqual(frontier.contains_state(1), True)
        self.assertEqual(frontier.remove(), node)

    def test_priority_queue_frontier(self):
        frontier = PriorityQueueFrontier()
        self.assertEqual(frontier.empty(), True)
        self.assertEqual(frontier.contains_state(1), False)
        node = Node(1)
        frontier.add(node)
        self.assertEqual(frontier.empty(), False)
        self.assertEqual(frontier.contains_state(1), True)
        self.assertEqual(frontier.remove(), node)

        frontier = PriorityQueueFrontier()
        node1 = Node(1, path_cost=1)
        node2 = Node(2, path_cost=2)
        frontier.add(node1)
        frontier.add(node2)
        self.assertEqual(frontier.remove(), node1)
        self.assertEqual(frontier.remove(), node2)

        frontier = PriorityQueueFrontier()
        node1 = Node(1, path_cost=2)
        node2 = Node(2, path_cost=1)
        frontier.add(node1)
        frontier.add(node2)
        self.assertEqual(frontier.remove(), node2)
        self.assertEqual(frontier.remove(), node1)

        frontier = PriorityQueueFrontier()
        node1 = Node(1, path_cost=2)
        node2 = Node(2, path_cost=2)
        frontier.add(node1)
        frontier.add(node2)
        self.assertEqual(frontier.remove(), node1)
        self.assertEqual(frontier.remove(), node2)

        frontier = PriorityQueueFrontier()
        node1 = Node(1, path_cost=1)
        node2 = Node(2, path_cost=1)
        frontier.add(node1)
        frontier.add(node2)
        self.assertEqual(frontier.remove(), node1)
        self.assertEqual(frontier.remove(), node2)

    def test_child_node(self):
        b1 = Bottle(8)
        b2 = Bottle(5)
        b3 = Bottle(3)
        node = Node(b1, b2, b3)
        child = node.child_node(problem=WaterBottleProblem, action="Fill bottle 1")
        self.assertEqual(child.state, Bottle(8, 8))
        self.assertEqual(child.parent, node)
        self.assertEqual(child.action, "Fill bottle 1")
        self.assertEqual(child.path_cost, 1)
        self.assertEqual(child.depth, 1)

if __name__ == "__main__":
    unittest.main()