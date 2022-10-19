#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.62%)
# Likes:    9458
# Dislikes: 421
# Total Accepted:    677.2K
# Total Submissions: 1.4M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    # First turn the input nums into a set of numbers.
    # The go through the numsbers. If the number x is the start of a streak,
    # then test y=v+1, v+2, v+3... and stop at the first number y not in the set.
    # The length of the streak is then simply y-v and we update our global best with that.
    # TC: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for v in nums:
            if v - 1 not in nums:
                y = v + 1
                while y in nums:
                    y = y + 1
                longest = max(longest, y - v)
        return longest
# @lc code=end

