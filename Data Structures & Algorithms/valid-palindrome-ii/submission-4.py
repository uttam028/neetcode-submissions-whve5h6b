class Solution:
    def validPalindrome(self, s: str) -> bool:
        mismatches = 0
        left = 0
        right = len(s)-1

        def isValidPalindrome(sub:str)->bool:
            l = 0
            r = len(sub)-1
            while(l<r):
                if(sub[l] != sub[r]):
                    return False
                l+=1
                r-=1
            return True


        while(left<right and mismatches < 2):
            if(s[left] == s[right]):
                left += 1
                right -= 1
                continue
            
            mismatches += 1
            further = isValidPalindrome(s[left+1:right+1]) or isValidPalindrome(s[left:right])
            if(not further):
                mismatches +=1
            break
        
        if(mismatches > 1):
            return False
        return True