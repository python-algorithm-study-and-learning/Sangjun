# 풀이 실패

import copy

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = []
        answer_route = float('inf')
        
        for i in range(0, n):
            queue = collections.deque([i])
            queue_len = len(queue)
            visited_node = [0] * n
            visited_node[i] = 1
            cur_list = []
            route = 0
            
            while len(queue):
                if route > answer_route:
                    break
                
                target = queue.popleft()
                
                for node in edges:
                    if target in node:
                        copy_node = copy.deepcopy(node)
                        copy_node.remove(target)
                        
                        if visited_node[copy_node[0]] == 0:
                            cur_list.append(copy_node[0])
                            visited_node[copy_node[0]] = 1
                    
                route += 1
                while len(cur_list):
                    queue.append(cur_list.pop())
                if sum(visited_node) == len(visited_node):
                    break
            
            cur_list = []
            
            if answer_route > route:
                answer = [i]
                answer_route = route
            elif answer_route == route: 
                answer.append(i)
            
        return answer
                