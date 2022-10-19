#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.59%)
# Likes:    6036
# Dislikes: 182
# Total Accepted:    399.6K
# Total Submissions: 898.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    # For each window representing a substring of s2 of length len(s1), 
    # we want to check if the count of the window is equal to the count of s1. 
    # Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]
    # We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). 
    # After, we only need to check if it is equal to the target. 
    # Working with list values of [0, 1,..., 25] instead of 'a'-'z' makes it easier to count later.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Cnt = [ord(x) - ord('a') for x in s1]
        s2Cnt = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        window = [0] * 26

        for x in s1Cnt:
            target[x] += 1
        for i, x in enumerate(s2Cnt):
            window[x] += 1
            if i >= len(s1Cnt):
                window[s2Cnt[i - len(s1Cnt)]] -= 1
            if window == target:
                return True
        return False
# @lc code=end

