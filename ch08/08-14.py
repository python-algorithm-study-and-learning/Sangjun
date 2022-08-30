# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_cur = list1
        list2_cur = list2
        answer = ListNode()
        answer_cur = answer
        
        while list1_cur and list2_cur:
            if list1_cur.val <= list2_cur.val: 
                answer_cur.next = ListNode(list1_cur.val)
                list1_cur = list1_cur.next
            else: 
                answer_cur.next = ListNode(list2_cur.val)
                list2_cur = list2_cur.next
            answer_cur = answer_cur.next
            
        if list1_cur: 
            answer_cur.next = list1_cur
        elif list2_cur: 
            answer_cur.next = list2_cur
            
        return answer.next