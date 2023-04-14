"""
You have three water bottles. 

Bottle #1 (b1) can be filled with 10 litres, 
Bottle #2 (b2) with 6 litres, 
Bottle #3 (b3) with 5 litres of water respectively. 

There are no markings on the bottles so you cannot measure them if 
the bottles are filled less than their maximum capacity. Assuming that you 
have an UNLIMITED SUPPLY OF WATER, by filling or emptying these three 
bottles: 
    (i)   How would you get from the start state to the end state? 
    (ii)  What is the solution with the fewest steps? 

    
The code should be able to solve this problem for the following parameters: 

a)  Start: b1 = 10, b2 = 0, b3 = 0 
    End: b1 = 0, b2 = 5, b3 = 5 
 
b)  Start: b1 = 3, b2 = 0, b3 = 0 
    End: b1 = 0, b2 = 1, b3 = 0 

c)  Start: b1 = 2, b2 = 0, b3 = 2 
    End: b1 = 9, b2 = 0, b3 = 0 
 
b) Repeat (c) but now change the maximum of the bottles [(i) b1: 11, b2: 1 b3: 3].  

"""
from classes.Problem import Problem
from classes.Node import *
from classes.Bottle import Bottle

import pydot
from IPython.display import Image, display


class WaterBottleProblem(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    # There are only two actions that can be performed on the bottles
    # 1. Fill a bottle
    # 2. Empty a bottle
    # The actions fuction returns the set of all possible actions that can be performed
    # on the bottles at a given state
    def actions(self, state):
        actions = []
        for bottle in state:
            if bottle.current < bottle.capacity:
                actions.append(("fill", bottle))
            if bottle.current > 0:
                actions.append(("empty", bottle))
        for bottle in state:
            for other_bottle in state:
                if bottle != other_bottle and bottle.current > 0 and other_bottle.current < other_bottle.capacity:
                    actions.append(("pour", bottle, other_bottle))
        return actions

    # The result function returns the state that the bottle transitions to as a result of an action
    def result(self, state, action):
        if action[0] == "fill":
            bottle: Bottle = action[1]
            difference = bottle.capacity - bottle.current
            bottle.fill(difference)
        elif action[0] == "empty":
            bottle: Bottle = action[1]
            bottle.current = 0
        elif action[0] == "pour":
            bottle: Bottle = action[1]
            other_bottle: Bottle = action[2]
            other_bottle.fill(bottle.current)
            bottle.current = 0
        return state

    # The h represents the heuristic function returns the number the tuples showing the difference between 
    # each bottle's current state and the goal state. use enumerate to get the index of the bottle
    def h(self, state):
        return sum([abs(bottle.current - self.goal[i]) for i, bottle in enumerate(state)])

    # The goal test function checks whether the state is the goal state
    # The goal state is when the bottles are filled with the capacities specified in the goal 
    def goal_test(self, state):
        # if each bottle in state has the current capacity equal to the goal tuple
        # then the state is the goal state. use enumerate to get the index of the bottle
        # in the state and the bottle in the goal tuple
        for i, bottle in enumerate(state):
            if bottle.current != self.goal[i]:
                return False

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError


