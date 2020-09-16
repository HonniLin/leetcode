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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :way
        A path from start to end, goes up on the tree for 0 or more steps, 
        then goes down for 0 or more steps. Once it goes down, it can't go up. 
        Each path has a highest node, which is also the lowest common ancestor of all other nodes on the path.
        A recursive method work(TreeNode node) 
            (1) computes the maximum path sum with highest node is the input node, update maximum if necessary 
            (2) returns the maximum sum of the path that can be extended to input node's parent.
        """
        self.res = float("-inf")
        def work(node):
            if not node:
                return 0
            left = max(work(node.left), 0)
            right = max(work(node.right), 0)
            cur = node.val + left + right
            self.res = max(self.res, cur)
            return node.val + max(left, right)
        work(root)
        return self.res