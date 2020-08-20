#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   shoukuai-1.py
@Time    :   2020/05/13 22:56:58
@Author  :   linhong02
@Desc    :   合并k个已排序数组
"""

import heapq
def merge(lists):
    heap = []
    for i, l in enumerate(lists):
        print i, l
        heap.append((l.pop(0),i))
    heapq.heapify(heap)
    result = []
    while heap:
        val, ids = heapq.heappop(heap)
        result.append(val)
        if lists[ids]:
            heapq.heappush(heap, (lists[ids].pop(0),ids))
    return result


lists = [[1,2,3], [2,3,4]]
print merge(lists)