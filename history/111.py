#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   111.py
@Time    :   2020/03/08 11:44:09
@Author  :   linhong02
@Desc    :   树 求最小深度
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        if root.left != None and root.right == None:
            return self.minDepth(root.left) + 1
        else: 
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1