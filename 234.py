#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   234.py
@Time    :   2020/04/05 16:31:43
@Author  :   linhong02
@Desc    :   None
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
