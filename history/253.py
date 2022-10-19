#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   253.py
@Time    :   2020/03/24 07:52:36
@Author  :   linhong02
@Desc    :   题目：给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

当我们遇到“会议结束”事件时，意味着一些较早开始的会议已经结束。我们并不关心到底是哪个会议结束。我们所需要的只是 一些 会议结束,从而提供一个空房间。
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0 or not intervals:
            return 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        user_room = 0
        L = len(intervals)
        end_point = 0
        start_point = 0
        while start_point < L:
            if start_timings[start_point] >= end_timings[end_point]:
                user_room -= 1
                end_point += 1
            user_room += 1
            start_point += 1
        return user_room

sol = Solution()
intervals = [[0, 30],[5, 10],[15, 20]]
intervals = [[5,8],[6,8]]
print sol.minMeetingRooms(intervals)