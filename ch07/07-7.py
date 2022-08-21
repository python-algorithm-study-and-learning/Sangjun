class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      sorted_nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
      from_idx, to_idx = 0, len(sorted_nums) - 1
      
      while sorted_nums[from_idx][1] + sorted_nums[to_idx][1] != target:
        sum = sorted_nums[from_idx][1] + sorted_nums[to_idx][1]
        if sum < target: 
          from_idx += 1
        if sum > target: 
          to_idx -= 1
      
      answer_from = sorted_nums[from_idx][0]
      answer_to = sorted_nums[to_idx][0]
      
      return [answer_from, answer_to]