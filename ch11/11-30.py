class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_list = []
        answer = 0
        
        for char in s:
            if char in my_list:
                target_idx = my_list.index(char)
                my_list = my_list[target_idx+1:]
            my_list.append(char)
            answer = max(len(my_list), answer)
            
        return answer