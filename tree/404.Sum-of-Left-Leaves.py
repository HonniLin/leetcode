#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   404.Sum-of-Left-Leaves.py
@Time    :   2020/10/26 23:58:42
@Author  :   linhong02
@Desc    :   None
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Recursive method. For given node we check whether its left child is a leaf. 
        If it is the case, we add its value to answer, otherwise recursively call method on left child. 
        For right child we call method only if it has at least one nonnull child.
        """
        self.res = 0
        def work(root, flag):
            if not root:
                 return 
            if not root.left and not root.right and flag == 0:
                self.res += root.val
            work(root.left, 0)
            work(root.right, 1)
        work(root, 1)
        return self.res