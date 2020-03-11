#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   114.py
@Time    :   2020/03/11 22:43:34
@Author  :   linhong02
@Desc    :   重点是在rtype, 需要在原树上面改。一颗一颗子树地拉直    
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if root.left == None and root.right == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp