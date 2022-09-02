# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        answer = answer_cur = ListNode()
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2: 
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_list.reverse()
        l2_list.reverse()
        
        sum = int(''.join(map(str,l1_list))) + int(''.join(map(str,l2_list)))
        
        if sum == 0:
            return answer
    
        
        while sum: 
            addr = sum % 10
            answer_cur.next = ListNode(addr)
            answer_cur = answer_cur.next
            sum = sum // 10
        
        return answer.next