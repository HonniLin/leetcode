# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#非递归
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = []
        stack = [(root,str(root.val))]
        while stack:
            node,num_sum = stack.pop()
            if node.left:
                stack.append((node.left,num_sum+str(node.left.val)))
            if node.right:
                stack.append((node.right,num_sum+str(node.right.val)))
            if not node.left and not node.right:
                res.append(int(num_sum))
        return sum(res)
        
#递归
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        def help(root, val, result):
            if root == None:
                return
            val = 10*val + root.val
            if not root.left and not root.right:
                result.append(val + result[-1])
                return
            if root.left:
                help(root.left, val, result)
            if root.right:
                help(root.right, val, result)
            
        val = 0
        result = [0]
        help(root, val, result)
        return result[-1]
