class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            current = set()
            current.add(s[i])
            for j in range(i+1, len(s)):
                if(s[j] in current):
                    break
                else:
                    current.add(s[j])
            if(len(current) > max):
                max = len(current)
        return max