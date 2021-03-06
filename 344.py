#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   344.py
@Time    :   2020/03/17 09:22:21
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i, j in zip(range(length - 1, -1, -1), range(length//2)):
            s[i], s[j] = s[j], s[i]

sol = Solution()
s = ["h","e","l","l","o"]
print sol.reverseString(s)