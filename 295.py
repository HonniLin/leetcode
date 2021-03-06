#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   295.py
@Time    :   2020/04/13 21:59:50
@Author  :   linhong02
@Desc    :   
思路2：
维护一个大顶堆和一个小顶堆 
两个优先级队列：
用于存储较小一半数字的最大堆 lo
用于存储较大一半数字的最小堆 hi
最大堆 lo 允许存储的元素最多比最小堆 hi 多一个。因此，如果我们处理了 kk 元素：
如果 k=2*n+1 \quad(\forall,n \in \mathbb z)k=2∗n+1(∀,n∈z) 则允许 lo 持有 n+1n+1 元素，而 hi 可以持有 nn 元素。
如果 k=2*n\quad(\forall,n\in\mathbb z)k=2∗n(∀,n∈z)，那么两个堆都是平衡的，并且每个堆都包含 nn 个元素。
这给了我们一个很好的特性，即当堆完全平衡时，中间值可以从两个堆的顶部派生。否则，最大堆 lo 的顶部保留合法的中间值。

添加一个数 num：
将 num 添加到最大堆 lo。因为 lo 收到了一个新元素，所以我们必须为 hi 做一个平衡步骤。因此，从 lo 中移除最大的元素并将其提供给 hi。
在上一个操作之后，最小堆 hi 可能会比最大堆 lo 保留更多的元素。我们通过从 hi 中去掉最小的元素并将其提供给 lo 来解决这个问题。
上面的步骤确保两个堆能够平衡

作者：LeetCode
链接：https://leetcode-cn.com/problems/find-median-from-data-stream/solution/shu-ju-liu-de-zhong-wei-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

python 小顶堆 https://www.cnblogs.com/lexus/p/3325000.html
"""

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = list()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self):
        """
        :rtype: float
        """
        leng = len(self.nums)
        if leng % 2 != 0:
            return self.nums[leng/2]
        else:
            return (self.nums[leng/2] + self.nums[leng/2 - 1]) / 2.0
 

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
print obj.findMedian()
obj.addNum(2)
print obj.findMedian()
obj.addNum(1)
print obj.findMedian()