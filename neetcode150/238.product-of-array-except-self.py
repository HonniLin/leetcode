#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (63.81%)
# Likes:    12245
# Dislikes: 742
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    # use tmp to store temporary multiply result by two directions.
    # Then fill it into result
    # TC: O(n) SC: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        if len_nums == 0:
            return []
        res = [1] * len_nums
        tmp = 1
        for i in range(len_nums):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len_nums - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res 
        
# @lc code=end

