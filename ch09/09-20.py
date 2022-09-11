class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesDict = {
            "(": ")",
            "{": "}", 
            "[": "]",
        }
        stack = [None]
        
        for char in s:
            last = stack[-1]
            try:
                if last and parenthesesDict[last] == char: 
                    stack.pop()
                else: 
                    stack.append(char)
            except KeyError:
                return False
                
        print(stack)
        if len(stack) == 1 and stack[0] == None:
            return True
        return False