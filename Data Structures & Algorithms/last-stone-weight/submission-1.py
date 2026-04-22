import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while(len(stones)>1):
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            diff = abs(x-y)
            if(diff>0):
                heapq._heappush_max(stones, diff)
        return 0 if len(stones)==0 else heapq._heappop_max(stones)
