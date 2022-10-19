#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   739.py
@Time    :   2020/04/06 15:44:02
@Author  :   linhong02
@Desc    :   单调栈
维护一个递增的栈，和栈顶元素做对比
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
sol = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print sol.dailyTemperatures(T)