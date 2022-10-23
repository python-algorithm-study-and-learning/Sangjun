# 풀이 실패 -> 나중에 풀이

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[float('inf')] * n for i in range(0, n)]
        shortest_path = [float('inf')] * n
        visited = [False] * n
        node_queue = []
        
        for route in times: 
            graph[route[0] - 1][route[1] - 1] = route[2]
        
        for i in range(0, n):
            graph[i][i] = 0
            
        shortest_path[k - 1] = 0
        
        def bfs(node):
            if visited[node - 1] == True:
                return
            visited[node - 1] = True
            idx = node - 1;
            next_path = graph[idx]
            for p_idx, p in enumerate(next_path): 
                shortest_path[p_idx] = min(shortest_path[p_idx], shortest_path[idx] + p)
            for node in range(0, n):
                if next_path[node] != 0 and next_path[node] != float('inf'):
                    node_queue.append(node)
            while node_queue:
                bfs(node_queue.pop(0) + 1)
            
        bfs(k)
        
        if max(shortest_path) == float('inf'):
            return -1
        return max(shortest_path)