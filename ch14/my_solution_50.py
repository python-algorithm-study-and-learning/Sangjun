# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        # [1, 2 ] [4, 5] 3 -> 루트 
        
        cur_idx = len(nums) // 2
        cur_node = TreeNode(nums[cur_idx])
        cur_left_idx = cur_idx // 2
        cur_right_idx = (len(nums) + cur_idx) // 2
        
        if cur_idx != cur_left_idx: 
            cur_node.left = self.sortedArrayToBST(nums[:cur_idx])
        if cur_idx != cur_right_idx: 
            cur_node.right = self.sortedArrayToBST(nums[cur_idx + 1:])
            
        return cur_node