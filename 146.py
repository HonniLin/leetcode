#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   146.py
@Time    :   2020/03/17 08:41:18
@Author  :   linhong02
@Desc    :   利用 OrderedDict 有序字典来更新元素的使用。元素被get时，把元素pop出，在放入。维持最近最少使用的元素在字典头
"""
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = OrderedDict()
        self.capacity = capacity 
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            value = self.dict.pop(key)
            self.dict[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dict.popitem(last = False)
        self.dict[key] = value

sol = LRUCache(2)
sol.put(1, 1)
sol.put(2, 2)
for k,v in sol.dict.items():
    print k,v

sol.get(2)
for k,v in sol.dict.items():
    print k,v
sol.put(3, 3)
for k,v in sol.dict.items():
    print k,v        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)