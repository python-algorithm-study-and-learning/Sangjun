class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        convert_paragraph = re.sub(r"[^a-z]+", ' ', paragraph.lower()).split()

        common_word_dict = dict()
        filter_banned_array = [i for i in convert_paragraph
                               if i not in banned]
        for element in filter_banned_array:
            if element in common_word_dict:
                common_word_dict[element] += 1
            else:
                common_word_dict[element] = 1

        return sorted(common_word_dict.items(), key=lambda x: x[1]).pop()[0]
