# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, None)
        temp = dummy
        curr = head.next
        curr_sum = 0

        while curr:
            if curr.val == 0:
                New = ListNode(curr_sum, None)
                temp.next = New
                temp = New
                curr_sum = 0
            curr_sum += curr.val

            curr = curr.next
        
        return dummy.next



            
        