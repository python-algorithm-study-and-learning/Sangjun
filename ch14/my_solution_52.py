# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer: int = 0
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if root: 
            if root.val > low:
                self.rangeSumBST(root.left, low, high)
            
            if root.val >= low and root.val <= high:
                self.answer += root.val 
            
            if root.val < high:
                self.rangeSumBST(root.right, low, high)
            
        return self.answer