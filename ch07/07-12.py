# 풀이 실패로 책에 나와있는 답안을 옮겨적었습니다
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신 
        for price in prices: 
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit

mySolution = Solution()
mySolution.maxProfit([2,1,2,1,0,1,2])
mySolution.maxProfit([7,1,5,3,6,4])