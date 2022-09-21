class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = []
        answer = 0
        
        for char in s:
            if char in my_set:
                target_idx = my_set.index(char)
                cur = 1
                my_set = my_set[target_idx+1:]
            my_set.append(char)
            answer = max(len(my_set), answer)
            
        return answer