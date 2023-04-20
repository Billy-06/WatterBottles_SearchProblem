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
from classes.Node import Node
from classes.Bottle import Bottle
from typing import Tuple, List

import pydot
from IPython.display import Image, display

class WaterBottleProblem(Problem):
    def __init__(self, initial: Node, goal: Tuple[int, int, int] =None):
        super().__init__(initial, goal)

    def __iter__(self):
        return iter(self.initial)
    
    def __repr__(self):
        return f"<WaterBottleProblem {self.initial}>"

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
        for bottle, goal  in zip(state, self.goal):
            if bottle.current > 0 or bottle.current > goal:
                for other_bottle in state:
                    if other_bottle != bottle:
                        actions.append(("pour", bottle, other_bottle))

                actions.append(("empty", bottle))
            if bottle.current < goal:
                actions.append(("fill", bottle))

        return actions
  
    # The result function returns the state that results from performing the action on the state
    # The action is a tuple with the first element being the action to be performed and the rest
    # being the arguments to the action
    # The state is a Node object containing 3 Bottle objects and their current volumes
    def result(self, state, action):
        # The action is a tuple with the first element being the action to be performed and the rest
        # being the arguments to the action
        action, *args = action
        # The state is a Node object containing 3 Bottle objects and their current volume
        b1, b2, b3 = state
        # If the action is to fill a bottle, then set the current volume of the bottle to the maximum volume
        if action == "fill":
            args[0].fill()
        # If the action is to empty a bottle, then set the current volume of the bottle to 0
        elif action == "empty":
            args[0].empty()
        # If the action is to pour a bottle into another bottle, then pour the current volume of the first
        # bottle into the second bottle until the second bottle is full or the first bottle is empty
        # whichever comes first
        elif action == "pour":
                args[0].pour(args[1])
        # # Return the new state as a Node object
        # return Node((b1, b2, b3))
        # Return the new state as a tuple
        return (b1, b2, b3)

    # The h represents the heuristic function returns the number the tuples showing the difference between 
    # each bottle's current state and the goal state. use enumerate to get the index of the bottle
    def h(self, state):
        return sum([abs(bottle.current - self.goal[i]) for i, bottle in enumerate(state)])

    # The goal_test function returns true if the state is equal to the goal state
    # and false otherwise. The state is a node object containing 3 Bottle objects and their current volumes
    # The goal state is a tuple containing the goal volumes for each bottle
    def goal_test(self, node: Node):
        return (node.state[0].current, node.state[1].current, node.state[2].current) == self.goal

    # The path_cost function returns the cost of the path from the initial state to the state
    # The cost is the number of steps taken to reach the state
    def path_cost(self, c, state1: Tuple[Bottle, Bottle, Bottle], action: str, state2: Tuple[Bottle, Bottle, Bottle]):
        return c + 1

    # The value function returns the value of the state
    # The value is the number of steps taken to reach the state
    def value(self):
        raise NotImplementedError
