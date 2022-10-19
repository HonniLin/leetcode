#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   743.Network-Delay-Time.py
@Time    :   2020/07/06 23:23:04
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        :desc 有 N 个网络节点，标记为 1 到 N。
给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。
现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。
        :way 从源节点到所有节点的最短路径 Dijkstra's算法
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dict = {node: float("inf") for node in xrange(1, N+1)}
        seen = [False] * (N + 1)
        dict[K] = 0
        while True:
            cand_node = -1
            cand_dict = float("inf")
            for i in xrange(1, N+1):
                if not seen[i] and cand_dict > dict[i]:
                    cand_dict = dict[i]
                    cand_node = i
            if cand_node == -1:
                break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dict[nei] = min(dict[nei], dict[cand_node] + d)
        ans = max(dict.values())
        return ans if ans < float("inf") else -1