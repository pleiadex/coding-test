# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils.Tree_Utils import TreeNode
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # both p and q are none
        if not p and not q:
          return True
        
        # either p or q is none
        if not p or not q or p.val != q.val:
          return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        