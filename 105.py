#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   105.py
@Time    :   2020/03/05 21:04:00
@Author  :   linhong02
@Desc    :   前序遍历：根-左-右
             中序遍历：左-根-右
             题意：根据前序和中序 构造树
             前序中找到根，在中序里以根为标记，分出左树和右树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        else:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root