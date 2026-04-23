class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []

        for interval in intervals:
            if(interval[1] < newInterval[0]):
                left.append(interval)
            elif(interval[0] > newInterval[1]):
                right.append(interval)
            else:
                # merge needed
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        # print(newInterval)
        left.append(newInterval)
        intervals = left + right
        return intervals