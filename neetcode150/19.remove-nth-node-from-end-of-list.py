#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from multiprocessing import dummy
from operator import le
import re


class Solution:
    # We are required to remove the nth node from the end of list. For this, we need to traverse N - n nodes from the start of the list, 
    # where N is the length of linked list. We can do this in one-pass as follows -
    # Let's assign two pointers - fast and slow to head. We will first iterate for n nodes from start using the fast pointer.
    # Now, between the fast and slow pointers, there is a gap of n nodes. Now, just Iterate and increment both the pointers till fast reaches the last node. 
    # The gap between fast and slow is still of n nodes, meaning that slow is nth node from the last node (which currently is fast).
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # delete
        left.next = left.next.next
        return dummy.next

# @lc code=end

