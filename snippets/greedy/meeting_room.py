'''
https://leetcode.com/problems/meeting-rooms-ii/#/description
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

idea:
1. sort the intervals by starting time. 
Iterate over the intervals, when seeing a new one, count++
Use a heap to maintain a end time list,
when the earlist end time is earlier than the cur start time, count--

2. Trick: make start time as 1, end time as -1
It is called sweep line from jiuzhang
http://www.jiuzhang.com/solution/number-of-airplanes-in-the-sky/
'''
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

def minMeetingRoom(intervals):
    intervals.sort(key=lambda x: x.start)
    end_time = [x.end for x in intervals]
    heapq.heapify(end_time)
    count = 0
    min_room = 0
    for interval in intervals:
        count += 1
        while end_time and end_time[0] <= interval.start:
            heapq.heappop(end_time)
            count -= 1
        min_room = max(min_room, count)
    return min_room


def sweepLine(intervals):
    def sorter(x, y):
        if x[0] == y[0]:
            return x[1] - y[1]
        else:
            return x[0] - y[0]
    timepoint = []
    for interval in intervals:
        timepoint.append((interval.start, 1))
        timepoint.append((interval.end, -1))
    timepoint.sort(cmp=sorter)
    count = 0
    min_room = 0
    for _, val in timepoint:
        count += val
        min_room = max(min_room, count)
    return min_room


if __name__ == '__main__':
    itvs = [[0, 30],[5, 10],[15, 20]]  # Need to make interval object here or change the code, trivially
    print(minMeetingRoom(itvs))
    print(sweepLine(itvs))