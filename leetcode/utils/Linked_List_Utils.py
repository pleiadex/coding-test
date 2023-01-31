from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertListToLinkedList(nums: List) -> Optional[ListNode]:
    if not nums:
        return None
    
    prev = ListNode(nums[-1])
    for n in nums[-2::-1]:
        curr = ListNode(n)
        curr.next = prev
        prev = curr
    
    return prev

def convertLinkedListToList(head: ListNode) -> List[int]: 
    node = head
    res = []
    while node:
        res.append(node.val)
        node = node.next

    return res