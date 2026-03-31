class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        reference = {}
        for i in range(len(s)):
            if s[i] in reference:
                reference[s[i]] += 1
            else:
                reference[s[i]] = 1
        for i in range(len(t)):
            if t[i] in reference:
                reference[t[i]] -= 1
            else:
                return False
        
        for key in reference.keys():
            if reference[key] != 0:
                return False
        return True
