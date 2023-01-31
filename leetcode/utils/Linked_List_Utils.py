from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertListToLinkedList(nums: List, pos=-1) -> Optional[ListNode]:
    head = ListNode()
    curr = head
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    
    if pos < 0:
        return head.next

    # generate a cycle
    joint = head
    while 0 <= pos and joint: 
        joint = joint.next
        pos -= 1

    curr.next = joint

    return head.next

def convertLinkedListToList(head: ListNode) -> List[int]: 
    node = head
    res = []
    while node:
        res.append(node.val)
        node = node.next

    return res


convertListToLinkedList([1,2], 0)