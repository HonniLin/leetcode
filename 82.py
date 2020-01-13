# coding=gbk
'''
@Author: your name
@Date: 2020-01-13 20:09:51
@LastEditTime : 2020-01-13 20:45:26
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /undefined/Users/linhong02/Documents/meme/code/leetcode/82.py
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        num = head.val - 1
        nodeH = ListNode(num)
        nodeH.next = head
        pre = nodeH
        cur = nodeH.next
        nodeH.next = head
        
        while cur != None:
            while cur.next and cur.next.val == pre.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return nodeH.next
        

sol = Solution()
print sol.deleteDuplicates()