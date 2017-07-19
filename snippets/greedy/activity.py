'''
Given a set of activities, each one has a start and end time and happens in [start, end)
Determine maximum number of activities can happen, where all activities are mutural compatible.abs

Invariants: array shoot balloon:
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/#/description

Idea:
Sort the intervals by ending time
Greedyly select the earlist finish interval
Skip all intervals that start before this end game
'''

def activity(lst):
    '''
    input: a list of intervals
    output: maximum compatible number of interval
    '''
    count = 1
    lst.sort(key=lambda x: x[1])
    end = lst[0][1]
    for i in range(1, len(lst)):
        if lst[i][0] < end: continue
        else:
            count += 1
            end = lst[i][1]
    return count


def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points: return 0
    points.sort(key=lambda x: x[1])
    end = points[0][1]
    count = 1
    for i in range(1, len(points)):
        if points[i][0] <= end: continue
        else:
            end = points[i][1]
            count += 1
    return count


if __name__ == '__main__':
    lst = [[10,16], [2,8], [1,6], [7,12]]
    print(activity(lst))
    print(findMinArrowShots(lst))