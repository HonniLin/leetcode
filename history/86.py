# coding=utf-8
'''
@Author: your name
@Date: 2020-02-11 19:55:23
@LastEditTime : 2020-02-11 20:15:07
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/86.py
分成两个链表记录，大数链表接到小数链表后边
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        small = ListNode(0)
        big = ListNode(0)
        res = small
        mid = big

        while head != None:
            node = head
            head = head.next
            if node.val < x:
                small.next = node
                small = small.next
            else:
                big.next = node
                big = big.next
        
        small.next = mid.next
        big.next = None

        return res.next

sol = Solution()
print sol.partition