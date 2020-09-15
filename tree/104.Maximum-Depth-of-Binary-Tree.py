# -*- encoding: utf-8 -*-
'''
@File    :   104.Maximum-Depth-of-Binary-Tree.py
@Time    :   2020/07/08 13:52:26
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :desc 求树的高度
        """
        """
        # 递归
        if not root:
            return 0
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            return max(left_h, right_h) + 1
        """
        # 非递归
        if not root:
            return 0
        stack = []
        stack.append((1, root))
        depth = 0
        while stack:
            cur_h, cur_n = stack.pop()
            if cur_n is not None:
                depth = max(depth, cur_h)
                stack.append((cur_h + 1, cur_n.left))
                stack.append((cur_h + 1, cur_n.right))
        return depth
        
