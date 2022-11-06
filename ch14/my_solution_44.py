# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_len: int = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None or (node.left is None and node.right is None): 
                return
            
            node.len = 0
            cur_max = 0
                    
            # 왼쪽 또는 오른쪽이 있는 경우 현재 노드와 값을 비교
            # 같은 숫자인 경우에는 len에 '자식 노드의 len + 1'을 더함
            if node.left:
                dfs(node.left)
                if node.left.val == node.val:
                    node.len = max(node.left.len + 1, node.len)
                    cur_max += node.left.len + 1
                    
            if node.right:
                dfs(node.right)
                if node.right.val == node.val:
                    node.len = max(node.right.len + 1, node.len)
                    cur_max += node.right.len + 1
                    
            # 최종적으로 값을 구하면, 둘 중 최대값을 max_len으로 설정함
            self.max_len = max(cur_max, self.max_len)
        
        # dfs를 직접 진행해본 뒤 값을 리턴함
        dfs(root)
        return self.max_len