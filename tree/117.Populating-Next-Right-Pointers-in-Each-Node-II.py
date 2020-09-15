#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   117.Populating-Next-Right-Pointers-in-Each-Node-II.py
@Time    :   2020/09/16 00:22:49
@Author  :   linhong02
@Desc    :   https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Connect the cur with every one of the possible nodes in child level, 
        update it only if the connected node is not nil.
        Do this one level by one level. The whole thing is quite straightforward.
        """
        res = root
        while root:
            cur = tmp = Node(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next
            root = tmp.next
        return res