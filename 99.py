#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   99.py
@Time    :   2020/03/03 21:51:39
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            if self.pre and self.pre.val > root.val:
                if not self.first:
                    self.first = self.pre
                self.second = root
            self.pre = root
            inOrder(root.right)
        
        inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val