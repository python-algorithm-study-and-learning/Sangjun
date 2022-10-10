# 풀이 실패 -> 나중에 다시 풀기

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        answer = True
        is_taken = [0] * numCourses
        
        def dfs(course):
            next_courses = graph[course]
            if len(next_courses) == 0:
                return
            for c in next_courses:
                if is_taken[c] != 0:
                    answer = False
                dfs(c)
        
        graph = collections.defaultdict(list)
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
            
        for i in range(0, numCourses):
            is_taken[i] += 1
            for course in graph[i]: 
                dfs(course)
                

            