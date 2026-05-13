class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_index = -1
        min_len = math.inf
        for i in range(len(strs)):
            if(len(strs[i]) < min_len):
                min_len = len(strs[i])
                min_index = i
        
        prefix = ''
        for i in range(len(strs[min_index])):
            ch = strs[min_index][i]
            more_prefix = True
            for j in range(len(strs)):
                if(strs[j][i] != ch):
                    more_prefix = False
                    break
            if(more_prefix):
                prefix += ch
            else:
                break
        return prefix