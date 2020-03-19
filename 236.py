#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   236.py
@Time    :   2020/03/19 09:22:05
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q) #没有找到的话就会返回None
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return node 
        if left and not right:
            return left
        if right and not left:
            return right