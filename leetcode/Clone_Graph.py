"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hmap = {}

        def clone(node):
            if node in hmap:
              return hmap[node]
            
            hmap[node] = Node(node.val)
            for n in node.neighbors:
              hmap[node].neighbors.append(clone(n))

            return hmap[node]

        return clone(node) if node else None