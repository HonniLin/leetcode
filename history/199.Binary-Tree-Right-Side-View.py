# -*- encoding: utf-8 -*-
'''
@File    :   199.Binary-Tree-Right-Side-View.py
@Time    :   2020/07/08 15:50:27
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :desc 输出树的右视图
        :way 深度优先搜索
        """
        if not root:
            return None 
        rightmost_value_at_depth = dict()
        stack = []
        stack.append((root, 0))
        max_depth = 0
        while stack:
            cur, depth = stack.pop()
            if cur:
                max_depth = max(depth, max_depth)
                rightmost_value_at_depth.setdefault(max_depth, cur.val)
                stack.append((cur.left, depth + 1))
                stack.append((cur.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]