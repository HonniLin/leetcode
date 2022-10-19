#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   310.Minimum-Height-Trees.py
@Time    :   2020/07/06 21:29:02
@Author  :   linhong02
@Desc    :   None
"""
from collections import defaultdict 
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        :desc 查找最小高度数的根节点
        :way bfs
        从边缘开始，先找到所有出度为1的节点，然后把所有出度为1的节点进队列，然后不断地bfs，最后找到的就是两边同时向中间靠近的节点，
        那么这个中间节点就相当于把整个距离二分了，那么它当然就是到两边距离最小的点啦，也就是到其他叶子节点最近的节点了。
        从最外层遍历,最后一层即为结果.
        """
        if n == 1:
            return [0]
        
        adjs = defaultdict(list)
        degrees = [0 for _ in range(n)]
        for f, t in edges:
            adjs[f].append(t)
            adjs[t].append(f)
            degrees[t] += 1
            degrees[f] += 1
        
        layer_queue = []
        for i in range(n):
            if degrees[i] == 1:
                layer_queue.append(i)
        
        while layer_queue:
            next_layer = []
            for node in layer_queue:
                for neighbor in adjs[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        next_layer.append(neighbor)
            if not next_layer:
                return layer_queue
            layer_queue = next_layer

sol = Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print sol.findMinHeightTrees(n, edges)


           

