# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myheap = []
        answer = ListNode()
        current = answer
        
        for _list in lists:
            head = _list
            while head: 
                heapq.heappush(myheap, head.val)
                head = head.next
                
        while len(myheap):
            value = heapq.heappop(myheap)
            current.next = ListNode()
            current = current.next
            current.val = value
            
        return answer.next