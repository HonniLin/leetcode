# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    :way 
    1/ get the array that contain the nodes of the binary search tree in the sorted order by inorder traversal
    2/ Whenever there's a call to hasNext, we check the length of array
    3/ For the call to next function, we simply return the top element of array
    """
    def __init__(self, root: TreeNode):
        self.tree_list = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.tree_list.append(root.val)
            inorder(root.right)
        inorder(root)
        print(self.tree_list)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.tree_list:
            return self.tree_list.pop(0)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.tree_list) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()