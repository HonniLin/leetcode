#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   109.py
@Time    :   2020/03/08 10:25:21
@Author  :   linhong02
@Desc    :   None
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        lens = len(nums)
        root = TreeNode(nums[lens/2])
        root.left = self.sortedArrayToBST(nums[0:lens / 2])
        root.right = self.sortedArrayToBST(nums[lens / 2 + 1: ])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        tmp = head
        while tmp:
            array.append(tmp.val)
            tmp = tmp.next
        return self.sortedArrayToBST(array)
        
        