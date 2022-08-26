from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiple_zeros = len([num for num in nums if num == 0]) >= 2
        total = reduce(lambda x, y: x * y, nums)
        answer = []
        
        if multiple_zeros: 
            return [0] * len(nums)
        elif total != 0: 
            for num in nums: 
                answer.append(total // num)
            return answer
        else:
            zero_index = nums.index(0)
            for (idx, num) in enumerate(nums):
                if idx == zero_index:
                    value = reduce(lambda x, y: x * y, [num for num in nums if num != 0])
                    answer.append(value)
                else: 
                    answer.append(0)
        
        return answer
        
mySolution = Solution([0,4,0])