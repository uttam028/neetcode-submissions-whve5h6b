"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        if(len(sorted_intervals) > 0):
            prev = sorted_intervals[0]
            for i in range(1, len(sorted_intervals)):
                curr = sorted_intervals[i]
                if(prev.end > curr.start):
                    return False
                prev = Interval(prev.start, curr.end)
        return True
