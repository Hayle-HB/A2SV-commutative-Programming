# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            if not head or not head.next:
                return True       
            slow = head
            fast = head
            stack = []
            
            while fast and fast.next:
                stack.append(slow.val)
                slow = slow.next
                fast = fast.next.next
            
            if fast:
                slow = slow.next
            
            while slow:
                if slow.val != stack.pop():
                    return False
                slow = slow.next
            
            return True
