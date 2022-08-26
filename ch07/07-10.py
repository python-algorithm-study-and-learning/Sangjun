class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([num[1] for num in enumerate(sorted(nums)) if num[0] % 2 == 0])