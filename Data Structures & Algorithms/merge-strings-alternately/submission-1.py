class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        base = ''
        other = ''
        if(len(word1) <= len(word2)):
            base = word1
            other = word2
        else:
            base = word2
            other = word1
        
        result = ''
        for i in range(len(base)):
            result += (word1[i] + word2[i])
        
        result += other[len(base):]
        return result