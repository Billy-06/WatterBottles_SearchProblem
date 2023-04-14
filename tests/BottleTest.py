from classes.Bottle import *
import unittest

# Write a test class that inherits from unittest.TestCase
# Test the following methods:
#   > __init__
#   > __repr__
#   > fill
#   > empty
#   > pour
class BottleTest(unittest.TestCase):
    def test_init(self):
        bottle = Bottle(5)
        self.assertEqual(bottle.capacity, 5)
        self.assertEqual(bottle.current, 0)

    def test_repr(self):
        bottle = Bottle(5)
        self.assertEqual(repr(bottle), "Bottle(capacity=5, current=0)")

    def test_fill(self):
        bottle = Bottle(5)
        bottle.fill(3)
        self.assertEqual(bottle.current, 3)

    def test_empty(self):
        bottle = Bottle(5)
        bottle.fill(3)
        bottle.empty()
        self.assertEqual(bottle.current, 0)

    def test_pour(self):
        bottle1 = Bottle(5)
        bottle2 = Bottle(3)
        bottle1.fill(3)
        bottle1.pour(bottle2)
        self.assertEqual(bottle1.current, 0)
        self.assertEqual(bottle2.current, 3)

    def test_pour2(self):
        bottle1 = Bottle(5)
        bottle2 = Bottle(3)
        bottle1.fill(5)
        bottle1.pour(bottle2)
        self.assertEqual(bottle1.current, 2)
        self.assertEqual(bottle2.current, 3)

if __name__ == '__main__':
    unittest.main()