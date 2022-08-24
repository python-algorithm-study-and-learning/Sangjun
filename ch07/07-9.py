class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums) - 2):
            from_num_idx = i + 1
            to_num_idx = len(sorted_nums) - 1
            
            while from_num_idx < to_num_idx:
                target_value = sorted_nums[i]
                first_value = sorted_nums[from_num_idx]
                second_value = sorted_nums[to_num_idx]
                
                if target_value + first_value + second_value < 0:
                    from_num_idx += 1
                elif target_value + first_value + second_value > 0:                    
                    to_num_idx -= 1
                else:
                    target_answer = (target_value, first_value, second_value)
                    answer.add(target_answer)
                    from_num_idx += 1
                    to_num_idx -= 1
        
        return [ list(tup) for tup in answer ][::-1]