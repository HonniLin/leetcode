#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   103.py
@Time    :   2020/03/04 21:39:13
@Author  :   linhong02
@Desc    :   层次遍历树，偶数层添加到尾部，奇数层添加到头部
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def work(self, head, res, index):
        if head == NULL:
            return
        if index >= len(res):
            res.append([])
        if index % 2 == 0:
            res[index].append(head.val)
        else:
            res[index].insert(0, head.val)
        self.work(head.left, res, index + 1)
        self.work(head.right, res, index + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.work(root, res, 0)
        return res