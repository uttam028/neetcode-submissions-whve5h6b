class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = len(prices)
        max = 0
        for i in range(num):
            for j in range(i+1, num):
                if(prices[j] - prices[i]) > max:
                    max = prices[j] - prices[i]
        return max