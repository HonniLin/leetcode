#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   141.py
@Time    :   2020/03/29 16:00:10
@Author  :   linhong02
@Desc    :   判断list是否为环
快慢指针
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
