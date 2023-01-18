"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        queue = deque([node])
        visited = [False] * 101
        hmap = {node: Node(node.val)}
        res = hmap[node]

        while queue:
            curr = queue.popleft()
            if curr and not visited[curr.val]:
                visited[curr.val] = True
                for n in curr.neighbors:
                    queue.append(n)

                if not curr in hmap:
                    hmap[curr] = Node(curr.val)
                for n in curr.neighbors:
                    if not n in hmap:
                        hmap[n] = Node(n.val)
                    hmap[curr].neighbors.append(hmap[n])
        return res

        