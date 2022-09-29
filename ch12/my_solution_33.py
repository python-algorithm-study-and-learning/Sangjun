class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        answer = []
        num_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        target = digits[0]
        previous_answer = self.letterCombinations(digits[1:])
        if len(previous_answer) == 0:
            for char in num_to_char[target]:
                answer.append(char)
        
        else:
            for char in num_to_char[target]:
                for prev in previous_answer:
                    answer.append(char + prev)
                
        return answer
            
            