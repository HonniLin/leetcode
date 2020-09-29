# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1/Start traversing the tree from the root node.
        2/If the current node itself is one of p or q, 
          we would mark a variable mid as True and continue the search for the other node in the left and right branches.
        3/If either of the left or the right branch returns True, this means one of the two nodes was found below.
        4/If at any point in the traversal, any two of the three flags left, right or mid become True, 
          this means we have found the lowest common ancestor for the nodes p and q.
        """
        self.ans = None
        def recurse_tree(cur_node):
            if not cur_node:
                return False
            left = recurse_tree(cur_node.left)
            right = recurse_tree(cur_node.right)
            mid = cur_node == p or cur_node == q
            if mid + left + right >= 2:
                self.ans = cur_node
            return mid or left or right
        recurse_tree(root)
        return self.ans