#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1345.Jump-Game-IV.py
@Time    :   2020/08/04 09:32:28
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        :desc bfs
        """
        from collections import defaultdict
        d = defaultdict(list)
        n = len(arr)

        for i in range(n):
            d[arr[i]].append(i)

        vis = [0] * n
        vis[0] = 1
        q = [(0, 0)]
        while q:
            i, k = q.pop(0)
            for j in d[arr[i]] + [i - 1, i + 1]:
                if j < 0 or j >= n or vis[j]:
                    continue
                if j == n - 1:
                    return k + 1
                vis[j] = 1
                q.append((j, k + 1))
            d[arr[i]] = [] # 访问过的删除，防止循环

        return 0