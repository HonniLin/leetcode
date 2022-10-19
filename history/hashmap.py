# coding=utf-8

def Hash_map_py(object):
    def __init__(self, length=10):
        self.length = length
        self.items = [[] for i in range(self.length)]

    def hash(self, key):
        return key % self.length
    
    def equals(self, key1, key2):
        return key1 == key2
    
    def insert(self, key, value):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0])
                    self.items[index].remove(item)
                    break
        self.items[index].append((key, value))
        return True
    
    def get(self, key):
        index = self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    return item[1]
        return False
