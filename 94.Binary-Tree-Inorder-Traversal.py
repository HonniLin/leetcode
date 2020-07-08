# -*- encoding: utf-8 -*-
'''
@File    :   94.Binary-Tree-Inorder-Traversal.py
@Time    :   2020/07/08 10:58:29
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :desc 中序遍历 非递归 栈
        """
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop() #此时左子树遍历完成
            res.append(top.val) #此时左子树遍历完成
            cur = cur.right #遍历右子树
        return res
                
            
        