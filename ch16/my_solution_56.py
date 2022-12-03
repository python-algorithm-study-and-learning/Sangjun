# 테케를 돌리면 맞췄다고 하는데, 정작 제출하면 똑같은 문제를 틀리게 함 (??)

class Trie:
    my_trie = collections.defaultdict(list)
    
    def insert(self, word: str) -> None:
        for i in range(0, len(word)): 
            if i != len(word) - 1: 
                self.my_trie[(i, word[i])].append((i + 1, word[i + 1]))
            if i == len(word) - 1: 
                self.my_trie[(i, word[i])].append(None)

    def search(self, word: str) -> bool:
        answer = True
        for i in range(0, len(word)):
            if i != len(word) - 1:
                if (i + 1, word[i + 1]) not in self.my_trie[(i, word[i])]:
                    return False 
            if i == len(word) - 1: 
                if None not in self.my_trie[(i, word[i])]:
                    return False
                
        return answer
            

    def startsWith(self, prefix: str) -> bool:
        answer = True
        
        if len(prefix) == 0:
            return True
        
        if len(self.my_trie.keys()) == 0: 
               return False
        
        for i in range(0, len(prefix)):
            if i != len(prefix) - 1:
                if (i + 1, prefix[i + 1]) not in self.my_trie[(i, prefix[i])]: 
                    return False
            
        return answer
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)