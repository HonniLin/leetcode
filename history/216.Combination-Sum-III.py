#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   216.Combination-Sum-III.py
@Time    :   2020/07/03 17:18:11
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        :desc 
            Find all possible combinations of k numbers that add up to a number n, 
            given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
        :way
            回溯
        """
        res_group = []
        def dfs(k, n, num, res):
            print res
            if k == 0 and n == 0:
                res_group.append(res)
                return 
            for i in range(num + 1, 10):
                dfs(k - 1, n - i, i, res + [i])
        dfs(k, n, 0, [])
        return res_group

sol = Solution()
k = 2
n = 18
print sol.combinationSum3(k, n)