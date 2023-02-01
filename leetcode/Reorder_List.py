# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from utils.Linked_List_Utils import ListNode
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        src = head
        dst = self.reverseList(slow)

        while dst.next:
            temp = src.next
            src.next = dst
            src, dst = dst, temp
        
        return

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp
        
        return prev    