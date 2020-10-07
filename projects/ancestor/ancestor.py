

from graph import Graph, Queue, Stack
from collections import defaultdict, deque

def earliest_ancestor(ancestors, starting_node):
    parent_child = {}

    for parent, child in ancestors:
        if child not in parent_child:
            parent_child[child] = set()

    parent_child[child].add(parent)

    earliest = -1 # because it testing for this

    stack = Stack()
# Adding first starting node to the stack
    stack.push(starting_node)

    while stack: # is not empty

        current = stack.pop()
        if current in parent_child:
            for parents in parent_child[current]:
                parents = parent

                if parent < parents:
                    parents = parent
                
                stack.push(parent)
            earliest = parents


    return earliest
                    
    


## CHECK:
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), 
                  (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)