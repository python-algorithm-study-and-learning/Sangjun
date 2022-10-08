class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        prev_numbers = []
        
        def dfs(n, k):
            if k == 0:
                answer.append(prev_numbers[:])
                return 
            
            if prev_numbers:
                start_point = prev_numbers[-1]
            else:
                start_point = 0
                
            for i in range(start_point + 1, n + 1):
                prev_numbers.append(i)
                dfs(n, k - 1)
                prev_numbers.pop()
        
        dfs(n, k)
        return answer