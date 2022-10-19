#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   399.Evaluate-Division.py
@Time    :   2020/07/06 22:55:39
@Author  :   linhong02
@Desc    :   None
"""

class WeightUnionFindSet:
    def __init__(self):
        self.parent = {}  # 存放父亲节点
        self.parent_div_cur = {} # 存放父亲节点除以自己的商

    def union(self, x, y, x_div_y):
        # 增加新节点
        if x not in self.parent:
            self.parent[x] = x
            self.parent_div_cur[x] = 1.0
        if y not in self.parent:
            self.parent[y] = y
            self.parent_div_cur[y] = 1.0
        
        # 寻找祖宗节点
        root_x, root_x_div_x = self.find_root(x)
        root_y, root_y_div_y = self.find_root(y)

        # 祖宗不同则进行合并
        if (root_x != root_y):
            self.parent[root_y] = root_x
            self.parent_div_cur[root_y] = root_x_div_x / root_y_div_y * x_div_y 
            # root_x / root_y = root_x / x / (root_y / y) * (x / y)
    
    def find_root(self, x):
        if self.parent[x] == x:
            return x, self.parent_div_cur[x]
        else:
            # 找到祖宗以及祖宗除以当前父节点的商
            root, root_div_parent = self.find_root(self.parent[x])
            # 路径压缩，并得到祖宗除以当前节点的商
            self.parent[x] = root
            self.parent_div_cur[x] = root_div_parent * self.parent_div_cur[x]
            return self.parent[x], self.parent_div_cur[x]

    def x_div_y(self, x, y):
        # x / y = root_y / y / (root_x / x)
        if x not in self.parent or y not in self.parent:
            return -1
        else:
            root_x, root_x_div_x = self.find_root(x)
            root_y, root_y_div_y = self.find_root(y)
            if root_x != root_y:
                return -1
            else:
                return root_y_div_y / root_x_div_x
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        weight_union_find_set = WeightUnionFindSet()

        # 加入并查集
        for (x, y), x_div_y in zip(equations, values):
            weight_union_find_set.union(x, y, x_div_y)
        
        # 查询并查集
        ans = []
        for x, y in queries:
            ans.append(weight_union_find_set.x_div_y(x, y))

        return ans