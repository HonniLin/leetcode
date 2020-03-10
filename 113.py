# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def work(self, root, sum, path, res):
        if not root:
            return res
        if not root.left and not root.right and root.val == sum:
            res.append(path + [root.val])
            return 
        self.work(root.left, sum - root.val, path + [root.val], res)
        self.work(root.right, sum - root.val, path + [root.val], res) 

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.work(root, sum, [], res)
        return res
