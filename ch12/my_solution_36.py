class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        prev_numbers = []
        
        def dfs(candidates, remains):
            if remains == 0:
                answer.append(prev_numbers[:])
            if remains < 0:
                return 
                
            for (idx, c) in enumerate(candidates):
                prev_numbers.append(c)
                dfs(candidates[idx:], remains - c)
                prev_numbers.pop()
        
        dfs(candidates, target)
        return answer