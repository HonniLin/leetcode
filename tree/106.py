#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   106.py
@Time    :   2020/03/07 21:47:32
@Author  :   linhong02
@Desc    :   用中序遍历和后续遍历(左右根) 构建树。类似105题，特点是找到后序的根位置在最后。
             所以从后往前遍历，确定根在中序的位置，将中序变成左右树再进行遍历。
             需要注意的是 后序的右根比左跟先找到
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        else:
            index = inorder.index(postorder.pop()):
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[0:index], postorder) 
            return root