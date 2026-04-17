class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for ch in s:
            if(ch.isalnum()):
                chars.append(ch.lower())
        for i in range(int(len(chars)/2)):
            if(chars[i] != chars[len(chars)-1-i]):
                return False
        return True

            