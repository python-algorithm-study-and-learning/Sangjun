# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 풀이 성공 -> 내가 더 빠름
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node_arr = []
        
        def dfs(root, lv):
            if not root: 
                return lv
            
            return max(dfs(root.left, lv + 1), dfs(root.right, lv + 1))
        
        return dfs(root, 0)