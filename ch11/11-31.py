class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = collections.defaultdict(int)
        
        for num in nums:
            my_dict[num] += 1
        
        items = list(my_dict.items())
        items.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in items[:k]]