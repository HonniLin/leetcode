#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   378.KthSmallestElementinaSortedMatrix.py
@Time    :   2020/07/18 00:44:50
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        :desc 求有序矩阵中的第k小的数
        :way 堆
        using Heap: O(min(K,N)+K∗logN)
        This problem can be easily converted to 'Kth Smallest Number in M Sorted Lists'.
        As each row (or column) of the given matrix can be seen as a sorted list, 
        we essentially need to find the Kth smallest number in ‘N’ sorted lists. 
        """
        minHeap = []
        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k, len(matrix))):
            heapq.heappush(minHeap, (matrix[i][0], 0, matrix[i]))

        # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
        # if the row of the top element has more elements, add the next element to the heap
        cnt, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            cnt += 1
            if cnt == k:
                break
            if len(row) > i + 1:
                heapq.heappush(minHeap, (row[i+1], i + 1, row))
        return number