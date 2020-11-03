# -*- encoding: utf-8 -*-
'''
@File    :   437.Path-Sum-III.py
@Time    :   2020/07/08 17:49:22
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        :desc 给定一个二叉树，它的每个结点都存放着一个整数值。
            找出路径和等于给定数值的路径总数。
            路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
        :way sumlist[]记录当前路径上的和
        """
        def dfs(root, sumlist):
           if not root:
               return 0
            sumlist = [num+root.val for num in sumlist]
            sumlist.append(root.val)
            count = 0
            for num in sumlist:
                if num == sum:
                    count += 1
            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])