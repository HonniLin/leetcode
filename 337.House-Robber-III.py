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
    def rob(self, root):
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
        return self.helper(root)[1]
    # helper函数返回一个节点为根的最大值 = [当前节点不参与计算的最大收益，当前节点的最大收益(参与/不参与)]
    def helper(self, root):
        if not root:
            return [0, 0]
        left_amount = self.helper(root.left)
        right_amount = self.helper(root.right)
        # 该节点偷，则左右节点不偷
        with_rob = left_amount[0] + right_amount[0] + root.val
        # 该节点不偷，则左右节点偷
        without_rob = left_amount[1] + right_amount[1]
        return [without_rob, max(with_rob, without_rob)]
        