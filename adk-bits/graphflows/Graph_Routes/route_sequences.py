'''

A sequential route runs each node once, in the listed order.

The edges array uses the START keyword to indicate the beginning of a graph execution, with each listed node executed in sequence:
'''

edges=[("START", task_A_node)]  # single node run
edges=[("START",
        task_A_node,
        task_B_node,
        task_C_node)]  # 3 nodes run in order

'''
In Python, branching is handled by a FunctionNode that returns an Event(route=...) value, which the edges dict dispatches to different nodes
'''
