# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            temp = 0
            if l1:
                temp+=l1.val
                l1 = l1.next
            if l2:
                temp+=l2.val
                l2 = l2.next
            if carry:
                temp+=1
                carry = False
            if temp>=10: carry = True
            return ListNode(val = temp%10, next=traverse(l1, l2, carry))
            
        return traverse(l1, l2, False)