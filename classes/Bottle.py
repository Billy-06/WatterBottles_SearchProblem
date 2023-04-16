# Define the Bottle class
class Bottle:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0

    def fill(self):
        self.current = self.capacity
        # self.current = amount

    def empty(self):
        self.current = 0

    def pour(self, other: object):
        if self.current > 0:
            # If the other bottle is empty, fill it
            if other.current == 0 and self.current > other.capacity:
                other.fill()
                self.current -= other.capacity
                assert self.current >= 0 and other.current <= other.capacity
            # If the other bottle is not empty, pour the contents of the current bottle into the other bottle
            # and empty the current bottle
            elif other.current == 0 and self.current < other.capacity:
                other.current = self.current
                self.empty()
                assert self.current >= 0 and other.current <= other.capacity
            # If the other bottle is not empty and the current bottle has more than enough to fill the other bottle
            # then fill the other bottle and subtract the amount that was poured from the current bottle
            elif other.current > 0 and self.current > other.capacity:
                self.current -= (other.capacity - other.current)
                other.fill()
                assert self.current >= 0 and other.current <= other.capacity
            # If the other bottle is not empty and the current bottle does not have enough to fill the other bottle
            # then fill the other bottle and empty the current bottle
            elif other.current > 0 and self.current < other.capacity:
                other.fill()
                self.empty()
                assert self.current >= 0 and other.current <= other.capacity
            elif other.current == other.capacity:
                return
        else:
            return

    def __repr__(self):
        return f"Bottle(capacity={self.capacity}, current={self.current})"
