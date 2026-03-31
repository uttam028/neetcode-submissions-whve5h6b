class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        reference = {}

        for i in range(len(s)):
            if s[i] in reference:
                reference[s[i]] += 1
            else:
                reference[s[i]] = 1

            if t[i] in reference:
                reference[t[i]] -= 1
            else:
                reference[t[i]] = -1

        for key in reference.keys():
            if reference[key] != 0:
                return False
        return True
