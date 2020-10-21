# -*- encoding: utf-8 -*-
'''
@File    :   337.House-Robber-III.py
@Time    :   2020/07/08 17:36:58
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
    def rob(self, root: TreeNode) -> int:
        def heaper(root):
            """
        :type root: TreeNode
        :rtype: int
        :desc 小偷在树上偷
        :way # 递归求解+DP
            # 当前节点取得最大收益取决于两个值，当前节点值，和上一层节点取得的最大收益
            # 当前节点取得最大收益的两种情况：
            # 1. 当前节点被计入，以及其孙子及更深的节点
            # 2. 当前节点未计入，其孩子及一些更深的节点
            # 因此，当前节点是否被计入到收益中，是这层节点如何取最大值的条件
            # 对于一个节点，我们只需要比较：它不参与计算时的最大值=其最左右节点最大值之和 VS 它参与计算=value+左右节点不参与结算时的最大值
        """
            if not root:
                return [0, 0]
            left = heaper(root.left)
            right = heaper(root.right)
            with_rot = left[0] + right[0] + root.val
            without_rot = max(left) + max(right)
            return [without_rot, max(with_rot, without_rot)]
        return max(heaper(root))
        