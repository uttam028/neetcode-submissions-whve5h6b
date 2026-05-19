class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        val = n
        for i in range(32):
            temp = val >> 1
            if(val - temp > temp):
                count+=1
            val = temp
        return count