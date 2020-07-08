# -*- encoding: utf-8 -*-
'''
@File    :   145.Binary-Tree-Postorder-Traversal.py
@Time    :   2020/07/08 15:40:34
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :desc 后序遍历 非递归
        """
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
                
            top = stack.pop()
            cur = top.left
        
        return res[::-1]
            