#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   907.SumofSubarrayMinimums.py
@Time    :   2020/07/14 21:16:31
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        :desc 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
              由于答案可能很大，因此返回答案模 10^9 + 7。
        :way 单调栈 
        https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/
        """
        A = [float("-inf")] + A + [float("-inf")]
        res = 0
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10**9 + 7)