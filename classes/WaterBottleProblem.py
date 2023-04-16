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
        # For each bottle in the state, compare the current volume with the goal volume
        # If the current volume is less than the goal volume, then the bottle can be filled
        # If the current volume is greater than 0, then the bottle can either be poured into another bottle
        # or emptied
        for i in zip(state, self.goal):
            if i[0].current < i[1]:
                actions.append(("fill", i[0]))
            if i[0].current > 0:
                for j in state:
                    if j != i[0]:
                        actions.append(("pour", i[0], j))

                actions.append(("empty", i[0]))
                        

        return actions

        
    # The result function returns the state that results from performing the action on the state
    # The action is a tuple with the first element being the action to be performed and the rest
    # being the arguments to the action
    # The state is a Node object containing 3 Bottle objects and their current volumes
    def result(self, state, action):
        # Create a copy of the state
        new_state = [Bottle(bottle.capacity) for bottle in state]
        for i, bottle in enumerate(state):
            new_state[i].current = bottle.current

        # Perform the action on the copy of the state
        if action[0] == "fill":
            action[1].fill()
        elif action[0] == "empty":
            action[1].empty()
        elif action[0] == "pour":
            action[1].pour(action[2])

        # Return the new state
        return tuple(new_state)

    # The h represents the heuristic function returns the number the tuples showing the difference between 
    # each bottle's current state and the goal state. use enumerate to get the index of the bottle
    def h(self, state):
        return sum([abs(bottle.current - self.goal[i]) for i, bottle in enumerate(state)])

    # The goal_test function returns true if the state is equal to the goal state
    # and false otherwise. The state is a node object containing 3 Bottle objects and their current volumes
    # The goal state is a tuple containing the goal volumes for each bottle
    def goal_test(self, state: Node):
        return state[0].current == self.goal[0] and state[1].current == self.goal[1] and state[2].current == self.goal[2]

    # The path_cost function returns the cost of the path from the initial state to the state
    # The cost is the number of steps taken to reach the state
    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError


