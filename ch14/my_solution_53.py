# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 왼 - 중 - 오 -> inorder (중위 순회)
# 제일 작은 수 -> 제일 큰 수 (1, 2, 3, 4, 6)

# 차이가 가장 작은 노드 -> 비교 -> 기준 -> 붙어있는 노드


class Solution:
    min_diff = float("inf")
    before_node = None
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 
        
        # 왼쪽
        self.minDiffInBST(root.left)
        
        # 루트 
        if self.before_node:
            self.min_diff = min(self.min_diff, root.val - self.before_node.val)
        self.before_node = root
        
        # 오른쪽
        self.minDiffInBST(root.right)
        
        return self.min_diff
