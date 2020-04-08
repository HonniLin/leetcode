#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   133.py
@Time    :   2020/04/08 21:35:18
@Author  :   linhong02
@Desc    :   图的深拷贝
dfs
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        lookup = {}
        def dfs(node):
            if not node:
                return 
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)

        