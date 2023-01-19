from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertListToTree(treeList: List) -> TreeNode:
    if not treeList:
      return None

    todoQueue = deque(treeList)
    root = TreeNode(todoQueue.popleft())
    nodeQueue = deque([root])

    while todoQueue:
      node = nodeQueue.popleft()

      if not node: 
        continue

      leftValue = todoQueue.popleft() if todoQueue else None
      rightValue = todoQueue.popleft() if todoQueue else None

      leftNode  = TreeNode(leftValue) if leftValue else None
      rightNode = TreeNode(rightValue) if rightValue else None
      node.left  = leftNode
      node.right = rightNode

      nodeQueue.append(leftNode)
      nodeQueue.append(rightNode)

    return root

def convertTreetoList(root: TreeNode) -> List[int]:
    if not root:
      return []

    queue = deque([root])
    res = []

    while queue:
      node = queue.popleft()
      
      res.append(node.val if node else None)
      
      if not node:
        continue

      queue.append(node.left)
      queue.append(node.right)

    for i in range(len(res) - 1, -1, -1):
      if not res[i]:
        res.pop()
      else:
        break

    return res
