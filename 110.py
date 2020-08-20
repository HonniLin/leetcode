#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   110.py
@Time    :   2020/03/08 10:55:46
@Author  :   linhong02
@Desc    :   树 求左右子树的深度差是否 > 1，是则不是平衡二叉树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root):
        if not root:
            return 1

        depth_left = self.depth(root.left)
        if depth_left == -1:
            return -1
        depth_right = self.depth(root.right)
        if depth_right == -1:
            return -1
        return 1 + max(depth_left, depth_right) if abs(depth_left - depth_right) <= 1 else -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1

        