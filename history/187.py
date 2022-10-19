#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   187.py
@Time    :   2020/04/20 23:29:57
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        visited = set()
        for i in range(0, len(s) - 9):
            tmp = s[i: i + 10]
            if tmp in visited:
                res.add(tmp)
            visited.add(tmp)
        return list(res)
        
sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print sol.findRepeatedDnaSequences(s)