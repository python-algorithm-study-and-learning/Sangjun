class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for from_idx in range(0, len(nums) - 1):
        for to_idx in range(from_idx + 1, len(nums)):
          if nums[from_idx] + nums[to_idx] == target:
            return [from_idx, to_idx]