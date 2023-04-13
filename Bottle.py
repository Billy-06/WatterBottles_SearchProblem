# Define the Bottle class
class Bottle:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0

    def fill(self):
        self.current = self.capacity

    def empty(self):
        self.current = 0

    def pour(self, other):
        other.current += self.current
        self.current = 0
        if other.current > other.capacity:
            self.current = other.current - other.capacity
            other.current = other.capacity

    def __repr__(self):
        return f"Bottle(capacity={self.capacity}, current={self.current})"
