class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for index, temp in enumerate(temperatures): 
            while len(stack) and temperatures[stack[-1]] < temp:
                ans_idx = stack.pop()
                answer[ans_idx] = index - ans_idx

            stack.append(index)
            
        return answer