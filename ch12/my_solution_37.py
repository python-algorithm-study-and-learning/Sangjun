class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(current, prev):
            if len(current) == 0:
                answer.append(prev[:])
            else:
                dfs(current[1:], prev[:])
                dfs(current[1:], prev[:] + [current[0]])
                
        dfs(nums, [])
        return answer