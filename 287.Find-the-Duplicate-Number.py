#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   287.Find-the-Duplicate-Number.py
@Time    :   2020/07/02 22:22:08
@Author  :   linhong02
@Desc    :   
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
链接：https://leetcode-cn.com/problems/find-the-duplicate-number

In this problem, nums[a] = b can be seen as a.next = b, 
the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.
有环链表求解交点

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder