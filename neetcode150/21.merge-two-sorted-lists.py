#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (61.66%)
# Likes:    15170
# Dislikes: 1331
# Total Accepted:    2.7M
# Total Submissions: 4.3M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # For simplicity, we create a dummy node to which we attach nodes from lists. 
    # We iterate over lists using two-pointers and build up a resulting list 
    # so that values are monotonically increased.
    # Time: O(n)
    # Space: O(1)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

# @lc code=end

