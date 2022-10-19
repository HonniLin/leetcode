#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   24.py
@Time    :   2020/05/17 12:19:39
@Author  :   linhong02
@Desc    :   链表左右节点交换
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
    
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

