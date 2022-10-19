#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1306.Jump-Game-III.py
@Time    :   2020/08/04 09:18:35
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        :desc dfs
        """
        if arr[start] == 0:
            return True
        n = len(arr)
        que = list()
        que.append(start)
        used = [start]
        while que:
            top = que.pop()
            for v in [top - arr[top], top + arr[top]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    used.append(v)
                    que.append(v)
        return False