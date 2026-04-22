class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            res = digits[i] + carry
            if(i == len(digits)-1):
                res +=1
            if(res >=10):
                carry = 1
            else:
                carry = 0
            digits[i] = res%10

        if carry == 1:
            digits.insert(0, 1)
        return digits 