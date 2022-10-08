# 풀이 실패 -> 나중에 다시 풀어봐야 함 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(0, len(nums)):
            target = nums[i]
            new_list = [x for x in nums if x != target]
            print(target, new_list)
            for l in self.permute(new_list):
                arr.append([target] + l)
        