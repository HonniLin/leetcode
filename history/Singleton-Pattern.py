#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Singleton-Pattern.py
@Time    :   2020/07/09 16:18:58
@Author  :   linhong02
@Desc    :   
单例模式 https://www.cnblogs.com/-qing-/p/10898623.html
"""

import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()