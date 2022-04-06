# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    frontier=util.Stack()
    start_state=problem.getStartState()
    goal_state=[]
    visited=[]
    parent={}
    trace={}
    frontier.push(start_state)
    while(frontier.isEmpty()!=True):
        top_state=frontier.pop()
        if(problem.isGoalState(top_state)):
            temp=top_state
            while(temp!=start_state):
                goal_state.append(trace[temp])
                temp=parent[temp]
            goal_state.reverse()
            return goal_state
        else:
            visited.append(top_state)
            succ=problem.getSuccessors(top_state)
            for x in succ:
                if x[0] not in visited:
                    frontier.push(x[0])
                    parent[x[0]]=top_state
                    trace[x[0]]=x[1]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier=util.Queue()
    start_state=problem.getStartState()
    parent={}
    trace={}
    goal_state=[]
    visited=[]
    visited.append(start_state)
    frontier.push(start_state)
    while(frontier.isEmpty()!=True):
        top_state=frontier.pop()
        if(problem.isGoalState(top_state)):
            temp=top_state
            while(temp!=start_state):
                goal_state.append(trace[temp])
                temp=parent[temp]
            goal_state.reverse()
            return goal_state
        succ=problem.getSuccessors(top_state)
        for x in succ:
            if x[0] not in visited:
                visited.append(x[0])
                frontier.push(x[0])
                parent[x[0]]=top_state
                trace[x[0]]=x[1]
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier=util.PriorityQueue()
    start_state=problem.getStartState()
    parent={}
    trace={}
    goal_state=[]
    visited={}
    frontier.push(start_state,0)
    visited[start_state]=0
    while(frontier.isEmpty()!=True):
        top_state=frontier.pop() 
        if(problem.isGoalState(top_state)):
            temp=top_state
            while(temp!=start_state):
                goal_state.append(trace[temp])
                temp=parent[temp]
            goal_state.reverse()
            return goal_state
        succ=problem.getSuccessors(top_state)
        for x in succ:
            temp_cost=visited[top_state]+x[2]
            if((x[0] not in visited) or (temp_cost<visited[x[0]])):
                visited[x[0]]=temp_cost
                frontier.update(x[0],temp_cost)
                parent[x[0]]=top_state
                trace[x[0]]=x[1]
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier=util.PriorityQueue()
    start_state=problem.getStartState()
    parent={}
    trace={}
    goal_state=[]
    visited={}
    frontier.push(start_state,heuristic(start_state,problem))
    visited[start_state]=heuristic(start_state,problem)
    while(frontier.isEmpty()!=True):
        top_state=frontier.pop() 
        if(problem.isGoalState(top_state)):
            temp=top_state
            while(temp!=start_state):
                goal_state.append(trace[temp])
                temp=parent[temp]
            goal_state.reverse()
            return goal_state
        succ=problem.getSuccessors(top_state)
        for x in succ:
            temp_cost=visited[top_state]+x[2]+heuristic(x[0],problem)-heuristic(top_state,problem)
            if((x[0] not in visited) or (temp_cost<visited[x[0]])):
                visited[x[0]]=temp_cost
                frontier.update(x[0],temp_cost)
                parent[x[0]]=top_state
                trace[x[0]]=x[1]
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
