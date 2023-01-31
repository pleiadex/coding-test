# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from utils.Linked_List_Utils import ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while slow and fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
            return True

        return False