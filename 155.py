#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   155.py
@Time    :   2020/04/05 15:09:20
@Author  :   linhong02
@Desc    :   最小栈
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.help = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.help) == 0 or x < self.help[-1]:
            self.help.append(x)
        else:
            self.help.append(self.help[-1])

    def pop(self):
        """
        :rtype: None
        """
        if len(self.data) > 0:
            self.help.pop()
            return self.data.pop()
                    
    def top(self):
        """
        :rtype: int
        """
        if len(self.data) > 0:
            return self.data[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.help:
            return self.help[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()