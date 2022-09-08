# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        init_node, prev_node = ans, ans.next;
        curr = 1
        
        # from_node의 위치를 정하기
        while curr < left:
            init_node, prev_node = prev_node, prev_node.next
            curr += 1
        
        next_node = prev_node.next
        
        while curr < right: 
            init_node.next, next_node.next, prev_node.next = next_node, init_node.next, next_node.next
            next_node = prev_node.next
            curr += 1
            
        return ans.next     