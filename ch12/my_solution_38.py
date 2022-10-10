# 풀이 실패 -> 다시 풀어야 함

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        
        def dfs(current_location, remain_tickets):
            if len(remain_tickets) == 0:
                answer.append(current_location)
                return
            
            answer.append(current_location)
            next_locations = sorted([x for x in remain_tickets if x[0] == current_location], key=lambda x: x[1])
            
            if len(next_locations) == 0:
                answer.pop()
                return    
            
            for l in next_locations:
                next_tickets = remain_tickets[:]
                next_tickets.remove(l)
                dfs(l[1], next_tickets)
            
        
        dfs("JFK", tickets)
        return answer[:len(tickets) + 1]
        