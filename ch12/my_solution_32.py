# 테스트 케이스는 전부 통과했지만, 알고리즘 풀이에서는 틀림

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_arr = []
        lands = []
        answer = 0
        next_point = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for idx1, row in enumerate(grid):
            for idx2, col in enumerate(row):
                if col == "1":
                    land_arr.append([idx1, idx2])
                    
        land_arr_str = list(map(lambda x: ''.join([str(x[0]), str(x[1])]), land_arr))
                                        
        while land_arr:
            lands.append(land_arr.pop())
            land_arr_str.pop()
            answer += 1
            while lands:
                cur_land = lands.pop()
                for np in next_point: 
                    np_str = ''.join([str(np[0] + cur_land[0]), str(np[1] + cur_land[1])])
                    if np_str in land_arr_str:
                        remove_idx = land_arr_str.index(np_str)
                        land_arr_str.remove(np_str)
                        del land_arr[remove_idx]
                        print(land_arr, land_arr_str)
                        lands.append([np[0] + cur_land[0], np[1] + cur_land[1]])
                
        return answer
            