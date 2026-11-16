# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        fastptr = head
        slowptr = head
        while(slowptr and fastptr and fastptr.next and fastptr.next.next):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if(slowptr == fastptr):
                return True
        return False