#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   124.py
@Time    :   2020/03/15 20:21:43
@Author  :   linhong02
@Desc    :   https://zhuanlan.zhihu.com/p/77863151
每次都求了当前给定的节点的左子树和右子树的最大值，和我们 maxPathSum 函数的逻辑是一样的。
所以我们利用一个全局变量，在考虑 helper 函数中当前 root 的时候，同时去判断一下包含当前 root 的路径的最大值。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = -888888
        def work(self, root):
            if not root:
                return 0
            left = max(work(root.left), 0)
            right = max(work(root.right), 0)
            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        work(root)
        return res