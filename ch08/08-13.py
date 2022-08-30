# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_arr = []
        current_pointer = head
        
        while current_pointer.next:
            val_arr.append(current_pointer.val)
            current_pointer = current_pointer.next
            
        val_arr.append(current_pointer.val)
        
        return val_arr == val_arr[::-1]
    
    