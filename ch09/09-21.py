# 풀이 실패로 문제에 나와있는 답변으로 대체함 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            if char in seen: 
                continue
            # 뒤에 봍일 문자가 남아 있다면 스택에서 제거 
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
  