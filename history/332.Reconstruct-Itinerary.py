#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   332.Reconstruct-Itinerary.py
@Time    :   2020/07/06 22:15:08
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        :desc 求有向图的欧拉路径，输出字典序最小的
            （ 欧拉路径：图G中的一条路径，能够通过图中的每一条边，并且每条边仅通过一次）
        :way dfs
        """
        from collections import defaultdict
        dest = defaultdict(list)
        for k, v in sorted(tickets)[::-1]: #倒序
            print k, v
            dest[k] += v,
        res = list()
        stack = ["JFK"]
        while stack:
            while dest[stack[-1]]:
                stack.append(dest[stack[-1]].pop())
                #print stack[-1] 
            res.append(stack.pop())
        return res[::-1]
        
sol = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print sol.findItinerary(tickets)
        
        