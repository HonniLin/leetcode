#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   145.Binary-Tree-Postorder-Traversal.py
@Time    :   2020/09/21 23:46:09
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :desc return the postorder traversal of its nodes' values iteratively
        :way pre-order traversal is root-left-right, and post order is left-right-root. 
            modify the code for pre-order to make it root-right-left, and then reverse the output so that we can get left-right-root .
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return res[::-1]