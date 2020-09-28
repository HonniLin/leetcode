# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :desc Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
        :way 
        1/Start traversing the tree from the root node.
        2/If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
        3/If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
        4/If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
        """
        par = root.val
        p_v = p.val
        q_v = q.val
        if p_v > par and q_v > par:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_v < par and q_v < par:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
