# coding=utf-8
'''
@Author: your name
@Date: 2020-02-19 21:50:56
@LastEditTime : 2020-02-19 22:36:56
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/98.py
way1: 棵树是二叉查找树，那么左子树的节点值一定处于（负无穷，root.val）这个范围内，右子树的节点值一定处于（root.val，正无穷）这个范围内。
     （注意边界值，负无穷和正无穷换成浮点型的极值）
way2: 中序遍历
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def heaper(root):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False

            return heaper(root.left, min, root.val) and heaper(root.right, root.val, max)

        if root is None:
            return True
        return heaper(root, -2147483648.1, 2147483648.1)

sol = Solution()
print 