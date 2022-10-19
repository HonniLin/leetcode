#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   107.py
@Time    :   2020/03/07 22:05:11
@Author  :   linhong02
@Desc    :   None
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def level(self, root, res, depth):
        if not root:
            return
        if depth >= len(res):
            res.append([])
        res[depth].append(root.val)
        self.level(root.left, res, depth + 1)
        self.level(root.right, res, depth + 1)

    def levelOrderBottom(self, root):
        """
        #:type root: TreeNode
        #:rtype: List[List[int]]
        """
        res = []
        self.level(root, res, 0)
        ress = res[::-1]
        return ress
