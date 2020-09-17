#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   144.py
@Time    :   2020/05/12 23:02:20
@Author  :   linhong02
@Desc    :   二叉树的前序遍历
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def preOrder(root, res):
            if not root:
                return []
            res.append(root.val)
            preOrder(root.left, res)
            preOrder(root.right, res)
            return res
        preOrder(root, res)
        return res

# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            cur = top.right
        return res
