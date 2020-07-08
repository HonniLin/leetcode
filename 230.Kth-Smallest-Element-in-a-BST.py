# -*- encoding: utf-8 -*-
'''
@File    :   230.Kth-Smallest-Element-in-a-BST.py
@Time    :   2020/07/08 16:53:44
@Author  :   yourname 
@Desc    :   
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        :desc 找二叉搜索树中第k小的元素
        :way 中序遍历 迭代
        """
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            k -= 1
            if k == 0:
                return top.val
            cur = top.right
        