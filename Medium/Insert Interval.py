'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
'''
from typing import List


## brute force
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            print(intervals, start, end, new_start, new_end)
            if end < new_start:
                # res.append([start, end])
                i += 1
                continue
            elif start > new_end:
                intervals.insert(i, [new_start, new_end])
                return intervals
            else:
                ## overall case and erase the merged interval
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                intervals.pop(i)
        intervals.append([new_start, new_end])
        return intervals


## optimal method

class SolutionTwo:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        i = 0
        res = []
        for start, end in intervals:
            # print(intervals, start, end, new_start, new_end)
            if end < new_start:
                res.append([start, end])
                i += 1
                continue
            elif start > new_end:
                res.append([new_start, new_end])
                return res + intervals[i:]
            else:
                ## overall case and erase the merged interval
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                i += 1
        res.append([new_start, new_end])
        return res
