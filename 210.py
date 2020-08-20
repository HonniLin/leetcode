#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   210.py
@Time    :   2020/05/06 21:24:37
@Author  :   linhong02
@Desc    :   
拓扑排序
"""
from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]
        topological_sorted_order = []
        while zero_indegree_queue:
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)
            if vertex in adj_list:
                for i in adj_list[vertex]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        zero_indegree_queue.append(i)
                    
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print sol.findOrder(numCourses, prerequisites)