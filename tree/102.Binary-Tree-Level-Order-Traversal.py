"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
desc:
Given a binary tree, return the level order traversal of its nodes' values
way:
Each time we add root.val into the list, and then look at left and right child.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS 时间O(n）空间O(h) 是树的高度
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return 
            if len(res) < depth:
                res.append([])
            res[depth - 1].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return res

# BFS O(n) O(n)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res