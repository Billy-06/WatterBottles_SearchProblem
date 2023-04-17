"""

The class Problem is an abstract class that defines the interface for a problem to be 
solved by a search algorithm. It has the following methods:

> __init__(self, initial, goal=None): initializes a problem instance with the initial 
state and a goal state (if provided).

> actions(self, state): this method is abstract and should be implemented by the subclasses 
of the Problem class. It returns a list of valid actions that can be taken in the given 
state.

> result(self, state, action): this method is abstract and should be implemented by the 
subclasses of the Problem class. It returns the state that results from taking the given 
action in the given state.

> goal_test(self, state): this method returns True if the given state is a goal state, 
False otherwise.

> path_cost(self, c, state1, action, state2): this method calculates the path cost of 
moving from state1 to state2 by taking action. It returns the current cost plus 1 
(assuming all actions have the same cost).

> value(self): this method is abstract and should be implemented by the subclasses of 
the Problem class. It returns the value of the current state.

"""


# > Formal Problem Representation of Puzzle
# - Defined by five components
#       a. Initial State
#       b. Actions - a description of all possible actions executable from
#                    the state s. action(s) should return all these possible actions
#       c. Transition Model - a formal description of what each action does.
#                    A function result(s, a) returns the state that s transitions to as a result of action a.
#                    > a, b and c implicitly define the state space which are all the possible states
#                    give the action and the transitions
#       d. Goal Test - A way of checking whether state s is the goal state.
#       e. Path Cost - the cost it takes to get to state s' from state s as a
#                    result or action a, this could be determined by using the function cost(s, a, s')
class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError