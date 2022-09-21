class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewels_set = set(jewels)
        for stone in stones:
            if stone in jewels_set:
                answer += 1 
        return answerw