class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_sets = set()
        for val in strs:
            str_sets.add(''.join(sorted(list(val))))

        strs_list = list(str_sets)
        answer = [[] for _ in range(len(strs_list))]

        for val in strs:
            answer[strs_list.index(''.join(sorted(list(val))))].append(val)

        return answer

