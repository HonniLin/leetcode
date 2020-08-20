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
    def level(self, root, dep, res):
        if not root:
            return
        if dep >= len(res):
            res.append([])
        res[dep].append(root)
        self.level(root.left, dep+1, res)
        self.level(root.right, dep+1, res)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = root
        res = []
        self.level(root, 0, res)
        for i in range(len(res)):
            for j in range(len(res[i])-1):
                res[i][j].next = res[i][j+1]
            #res[i][len(res[i] - 1)].next = NULL
        
        return head

# Way：使用队列
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            count = len(queue)  #这一层的节点数
            while count>0:
                node1 = queue.pop(0)
                count -= 1
                if node1.left:
                    queue.append(node1.left)
                if node1.right:
                    queue.append(node1.right)
                if count > 0: #每一层的最后一个无需修改next指针
                    node1.next = queue[0]
        return root