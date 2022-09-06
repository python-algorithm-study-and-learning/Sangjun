# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        odd_cur = odd
        even_cur = even
        cur = head
        
        isOdd = True
        
        while cur:
            if isOdd:
                odd_cur.next = ListNode()
                odd_cur = odd_cur.next
                odd_cur.val = cur.val
            else: 
                even_cur.next = ListNode()
                even_cur = even_cur.next
                even_cur.val = cur.val
            isOdd = not isOdd
            cur = cur.next
            
        odd_cur.next = even.next
        
        return odd.next