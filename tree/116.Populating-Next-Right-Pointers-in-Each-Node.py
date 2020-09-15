#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   116.py
@Time    :   2020/03/15 11:27:46
@Author  :   linhong02
@Desc    :   None
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Way 1：把树按层级处理出来，
class Solution(object):
    def connect(self, root: 'Node') -> 'Node':
        res = []
        def work(root, level):
            if not root:
                return None
            if len(res) <= level:
                res.append([])
            if len(res[level]) > 0:
                tmp = res[level].pop()
                tmp.next = root
            res[level].append(root)
            work(root.left, level + 1)
            work(root.right, level + 1)
        work(root, 0)
        return root
        
# it's easy to come up with a very standard BFS solution using queue. But because of next pointer, 
# we actually don't need a queue to store the order of tree nodes at each level, 
# we just use a next pointer like it's a link list at each level;
# Time:O(n) Mem:O(1)
class Solution(object):
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        nex = cur.left
        while nex:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nex
                nex = cur.left
        return root