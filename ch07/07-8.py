class Solution:
    def trap(self, height: List[int]) -> int:
        max_point = max(height)
        max_point_idx = [i[0] for i in enumerate(height) if i[1] == max_point]
        answer = 0
      
        current_max = 0
        for i in range(0, max_point_idx[0]):
            current_point = height[i]
            if current_max < current_point:
                current_max = current_point
            else:
                answer += current_max - current_point
                
        current_max = 0
        for i in range(len(height) - 1, max_point_idx[-1], -1):
            current_point = height[i]
            if current_max < current_point:
                current_max = current_point
            else:
                answer += current_max - current_point
      


        # case 1 : 최댓값 지점이 1개인 경우
        if len(max_point_idx) == 1:
          return answer
      
        
        # case 2 : 최댓값 지점이 여러 개인 경우
        if len(max_point_idx) > 1:
            # 최댓값 지점 사이의 빗물 양도 계산해야 됨
            for i in range(max_point_idx[0], max_point_idx[-1]):
                answer += max_point - height[i]
            return answer
        
mySol = Solution()
mySol.trap([0,1,0,2,1,0,1,3,2,1,2,1])