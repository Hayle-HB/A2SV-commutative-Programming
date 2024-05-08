# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #creating two pointer

        slow = fast = head

        while fast is not None and fast.next is not None:
            #move the slow by one step
            slow = slow.next
            #move the fast by two ste
            fast = fast.next.next
        
        return slow
        