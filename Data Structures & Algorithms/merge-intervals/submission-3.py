class Solution:
    def insert(self, intervals: List[List[int]], newInterval:List[int])-> List[List[int]]:
        left = []
        right = []
        print(newInterval, intervals)
        for interval in intervals:
            if(interval[1] < newInterval[0]):
                left.append(interval)
            elif(interval[0] > newInterval[1]):
                right.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        left.append(newInterval)
        return left + right

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        ref = []
        for interval in intervals:
            ref = self.insert(ref, interval)
            # print(ref)
        return ref
