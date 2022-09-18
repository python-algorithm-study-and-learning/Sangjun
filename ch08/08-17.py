# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        first = head
        second = None
        if head.next:
            second = head.next 
        
        if second == None:
            return head
        
        while first.next.next and second.next.next:
            first.val, second.val = second.val, first.val 
            first = first.next.next 
            second = second.next.next
            
        first.val, second.val = second.val, first.val
            
        return head
    