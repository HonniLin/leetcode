#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   23.py
@Time    :   2020/05/17 11:46:19
@Author  :   linhong02
@Desc    :   合并k个有序链表
"""
#way 1：优先队列
# 时间复杂度：O(n*log(k))O(n∗log(k))，n 是所有链表中元素的总和，k 是链表个数。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(0)
        p = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, idx = heapq.heappop(heap)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

# way2
# 分而治之，链表两两合并

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)

    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

sol = Solution()
lists = [
    [1, 2, 3],
    [2, 3, 4]
]
print sol.mergeKLists(lists)

