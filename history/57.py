'''
@Author: your name
@Date: 2019-11-17 10:50:51
@LastEditTime: 2019-11-17 12:35:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/57.py
题意：将新的interval加入到interval列表中，并得到最新的列表
解法：把interval加入得到列表中，按照左坐标排序。遍历
'''
class Solution(object):
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        #print intervals
        res = []
        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size - 1][0] <= intervals[i][0] <= res[size - 1][1]:
                    res[size - 1][1] = max(res[size - 1][1], intervals[i][1])
                else:
                    res.append(intervals[i])
        return res

# O(nlgn) time, the same as Merge Intervals 
# https://leetcode.com/problems/merge-intervals/
def insert1(self, intervals, newInterval):
    intervals.append(newInterval)
    res = []
    for i in sorted(intervals, key=lambda x:x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res
    
# O(n) time, not in-place, make use of the 
# property that the intervals were initially sorted 
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i.end < n.start:
            res.append(i)
        elif n.end < i.start:
            res.append(n)
            return res+intervals[index:]  # can return earlier
        else:  # overlap case
            n.start = min(n.start, i.start)
            n.end = max(n.end, i.end)
    res.append(n)
    return res


if __name__ == "__main__":
    intervals = [[6,9], [1,3]]
    newInterval = [2,5]
    sol = Solution()
    print sol.insert(intervals, newInterval)