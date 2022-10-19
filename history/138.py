#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   138.py
@Time    :   2020/03/16 07:57:28
@Author  :   linhong02
@Desc    :   遍历原来的链表并拷贝每一个节点，将拷贝节点放在原来节点的旁边，创造出一个旧节点和新节点交错的链表。
迭代这个新旧节点交错的链表，并用旧节点的 random 指针去更新对应新节点的 random 指针。比方说， B 的 random 指针指向 A ，意味着 B' 的 random 指针指向 A' 。
现在 random 指针已经被赋值给正确的节点， next 指针也需要被正确赋值，以便将新的节点正确链接同时将旧节点重新正确链接。

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        # 复制节点在旁边
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        # 连接random节点
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        
        # 解链
        ptr_old_list = head
        ptr_new_list = head.next
        res = ptr_new_list
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next is not None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return res
            