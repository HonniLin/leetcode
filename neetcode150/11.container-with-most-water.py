#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.97%)
# Likes:    17115
# Dislikes: 955
# Total Accepted:    1.5M
# Total Submissions: 2.8M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    # https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
    # The widest container (using first and last line) is a good candidate, because of its width. 
    # Its water level is the height of the smaller one of first and last line.
    # Variables i and j define the container under consideration. 
    # We initialize them to first and last line, meaning the widest container. 
    # Variable water will keep track of the highest amount of water we managed so far. 
    # We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. \\
    # Multiply them to get how much water this container can hold, and update water accordingly. 
    # Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". 
    # Continue until there is nothing left to consider, then return the result.
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
# @lc code=end

