#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   207.Course-Schedule.py
@Time    :   2020/07/06 17:01:23
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        :desc 课程表 numCourses表示课程数 
        :way 拓扑排序
        """
        n = numCourses
        ind = [0 for _ in range(n)]
        link_table = [[] for _ in range(n)]
        for cur, pre in prerequisites:
            ind[cur] += 1
            link_table[pre].append(cur)
        queue = list()
        for i in range(n):
            if ind[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            numCourses -= 1
            for i in link_table[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    #link_table[node].remove(i)
                    queue.append(i)
        return not numCourses
        
sol = Solution()
numC = 2
prerequisites = [[1, 0], [0, 1]]
print sol.canFinish(numC, prerequisites)