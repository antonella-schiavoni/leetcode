# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

"""
The problem is resolved in a single pass using the Two-Pointer Technique with a Sentinel (Dummy) Node to establish an $n$-node gap between a slow and a fast pointer, guaranteeing the slow pointer stops exactly at the predecessor of the $n^{th}$ node from the end.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    
    dummy = ListNode(0)
    dummy.next = head
    
    slow = dummy
    fast = dummy
    
    for _ in range(n+1):
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    
    return dummy.next
            
        
