# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer_cur = None
        while head:
            answer_cur, answer_cur.next, head = head, answer_cur, head.next
        
        return answer_cur