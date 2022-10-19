#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.86%)
# Likes:    13416
# Dislikes: 601
# Total Accepted:    2.3M
# Total Submissions: 5.6M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    # Iterate through string until empty
    # Push any open parentheses onto stack
    # Check stack for corresponding closing parentheses, return false if not valid
    # return True if not open parentheses left in stack
    # TC: O(n)
    def isValid(self, s: str) -> bool:
        parenthesesMap = { ")": "(", "}": "{", "]": "[" }  
        stack = []
        for c in s:
            if c not in parenthesesMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != parenthesesMap[c]:
                return False
            stack.pop()
        return not stack 
# @lc code=end

