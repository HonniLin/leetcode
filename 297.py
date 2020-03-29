#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   297.py
@Time    :   2020/03/29 15:16:21
@Author  :   linhong02
@Desc    :   对树的序列号和反序列化
前序遍历进行序列化https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-leet/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        res = str(root.val) + '_'
        while len(queue) > 0:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                res += str(node.left.val) + '_'
            else:
                res += '#_'
            if node.right:
                queue.append(node.right)
                res += str(node.right.val) + '_'
            else:
                res += '#_'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split('_')
        queue = deque()
        root = TreeNode(int(arr[0]))
        queue.append(root)
        i = 1
        # 最后一个字符为''，因此无需判断
        while i < len(arr) - 1:
            node = queue.popleft()
            if arr[i] != '#':
                left = TreeNode(int(arr[i]))
                node.left = left
                queue.append(left)
            if i + 1 < len(arr) - 1 and arr[i + 1] != '#':
                right = TreeNode(int(arr[i + 1]))
                node.right = right
                queue.append(right)
            i += 2
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))