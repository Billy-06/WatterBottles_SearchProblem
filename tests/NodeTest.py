import unittest
from classes.Node import *
from classes.Problem import *

# Write a test class that inherits from unittest.TestCase
# Test the following methods in the Node class:
#   > __init__
#   > __repr__
#   > __lt__
#   > expand
#   > child_node
#   > solution
#   > path
class NodeTest(unittest.TestCase):
    def test_init(self):
        node: Node = Node(1)
        self.assertEqual(node.state, 1)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.action, None)
        self.assertEqual(node.path_cost, 0)
        self.assertEqual(node.depth, 0)

    def test_repr(self):
        node = Node(1)
        self.assertEqual(repr(node), "<Node 1>")

    def test_lt(self):
        node1 = Node(1)
        node2 = Node(2)
        self.assertTrue(node1 < node2)

    def test_expand(self):
        node = Node(1)
        problem = Problem(1, 2, 3)
        self.assertEqual(node.expand(problem), [Node(2), Node(3)])

    def test_child_node(self):
        node = Node(1)
        problem = Problem(1, 2, 3)
        self.assertEqual(node.child_node(problem, 2), Node(2))

    def test_solution(self):
        node = Node(1)
        self.assertEqual(node.solution(), [])

    def test_path(self):
        node = Node(1)
        self.assertEqual(node.path(), [Node(1)])

if __name__ == '__main__':
    unittest.main()