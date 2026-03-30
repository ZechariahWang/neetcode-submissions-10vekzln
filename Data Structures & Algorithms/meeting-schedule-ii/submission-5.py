"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events=[]

        for i in intervals:
            events.append((i.end, -1))
            events.append((i.start,1))

        res=0
        curr=0
        events.sort()

        for meeting_type, amount in events:
            curr+=amount
            res=max(res,curr)
        
        return res
        


        