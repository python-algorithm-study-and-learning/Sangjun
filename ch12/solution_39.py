# 풀이 1: DFS로 순환 구조 판별
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # make graph 
        for x, y in prerequisites: 
            graph[x].append(y)
            
        traced = set()
            
        def dfs(i):
            if i in traced: 
                return False
            
            traced.add(i)
            for np in graph[i]:
                if not dfs(np):
                    return False 
            traced.remove(i)
            
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False 
            
        return True

# 풀이 2: 가지치기를 이용한 최적화 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # make graph 
        for x, y in prerequisites: 
            graph[x].append(y)
            
        traced = set()
        visited = set()
            
        def dfs(i):
            if i in traced: 
                return False
            if i in visited:
                return True
            
            traced.add(i)
            for np in graph[i]:
                if not dfs(np):
                    return False 
            traced.remove(i)
            visited.add(i)
            
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False 
            
        return True
            
            