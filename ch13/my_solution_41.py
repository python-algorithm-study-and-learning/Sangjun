# 풀이 실패 (이유: 시간 초과 -> 80까지는 Accepted 되었으나 90부터 안됨)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = []
        visited = []
        remains = k

        # 가장 먼저 dict를 만든다. 
        routes = collections.defaultdict(list)
        
        for f in flights: 
            routes[f[0]].append([f[1], f[2]])
            
            
        # dfs를 이용해서 값을 계산한다
        def dfs(current, remains, acc):            
            # 초기화
            next_routes = routes[current]
            min_from_now = float('inf')
            
            if ans: 
                min_from_now = min(ans)
                
            # 끝나는 상황 처리
            if current in visited or remains < 0 or min_from_now < acc:
                return
            
            # 갱신 
            if current == dst:
                ans.append(acc)
                return
            
            visited.append(current)
            for next_route in next_routes:
                dfs(next_route[0], remains - 1, acc + next_route[1])
            visited.pop()
                    
        dfs(src, k + 1, 0)

        if not ans: 
            return -1
        return min(ans)