"""

The class is defined with an __init__ method that takes a single argument, capacity, 
which is used to initialize the capacity of the bottle object. It also initializes the 
current attribute of the object to 0, which represents the amount of water currently 
in the bottle.

The class also includes three methods: 
    > fill(), 
    > empty(), and 
    > pour(). 
The fill() method 
fills the bottle to its maximum capacity. The empty() method empties the bottle by setting
the current attribute to 0.

The pour() method is the most complex of the three methods. It takes an argument, other, 
which represents the bottle into which the current bottle will be poured. The method 
implements the logic of pouring water from the current bottle to the other bottle, taking 
into account the current water levels in both bottles.

The pour() method first checks if the current bottle is not empty. If the other bottle is 
empty and the current bottle has more water than the other bottle's capacity, it fills the 
other bottle and subtracts the capacity of the other bottle from the current bottle's 
water level. If the other bottle is empty but the current bottle has less water than the 
other bottle's capacity, it fills the other bottle with the current bottle's water and 
empties the current bottle. If the other bottle is not empty and the current bottle has 
enough water to fill the other bottle, it fills the other bottle and subtracts the 
difference between the other bottle's capacity and its current water level from the 
current bottle's water level. If the other bottle is not empty and the current bottle 
does not have enough water to fill the other bottle, it fills the other bottle with the 
current bottle's water and empties the current bottle.

The __repr__ method is used to define the string representation of the Bottle object. It 
returns a string with the capacity and current water level of the bottle object.

"""

# Define the Bottle class
class Bottle:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0

    def __name__(self):
        return f"Bottle({self.capacity})"
    
    def __repr__(self):
        return f"Bottle(capacity={self.capacity}, current={self.current})"
    
    def copy(self):
        return Bottle(self.capacity)

    def fill(self):
        self.current = self.capacity
        # self.current = amount

    def empty(self):
        self.current = 0

    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, Bottle) and self.current == __value.current and self.capacity == __value.capacity

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

