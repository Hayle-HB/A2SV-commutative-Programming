# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next