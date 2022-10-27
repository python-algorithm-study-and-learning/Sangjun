# 풀이 1: 파이썬다운 방식 
class Solution_1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: 
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root 
        return None
    
# 풀이 2: 반복 구조로 BFS
class Solution_2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue: 
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑 
            if node: 
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
                
        return root 
    
# 풀이 3: 반복 구조로 DFS 
class Solution_3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        
        while stack: 
            node = stack.pop()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)
                
        return root
    

# 풀이 4: 반복 구조로 DFS 후위 순회 
class Solution_4:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            
            if node: 
                stack.append(node.left)
                stack.append(node.right)
                
                node.left, node.right = node.right, node.left # 후위 순회 
                
        return root 
    