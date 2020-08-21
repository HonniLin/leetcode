'''
@Author: your name
@Date: 2020-02-17 21:58:22
@LastEditTime : 2020-02-17 22:12:11
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/96.py
二叉查找树的构造 递归
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        :I start by noting that 1..n is the in-order traversal for any BST with nodes 1 to n. 
        So if I pick i-th node as my root, the left subtree will contain elements 1 to (i-1), 
        and the right subtree will contain elements (i+1) to n. 
        I use recursive calls to get back all possible trees for left and right subtrees and combine them in all possible ways with the root.

        """
        def dfs(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                left_node = dfs(left, i - 1)
                right_node = dfs(i + 1, right)
                for leftn in left_node:
                    for rightn in right_node:
                        root = TreeNode(i)
                        root.left = leftn
                        root.right = rightn
                        res.append(root)
            return res
        if n == 0:
            return []
        return dfs(1, n)
                