#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (70.49%)
# Likes:    13300
# Dislikes: 506
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    # Use two integers to count the remaining left parenthesis and the right parenthesis to be added. 
    # At each function call add a left parenthesis if openCnt >0 and add a right parenthesis if closeCnt>0. 
    # Append the result and terminate recursive calls when both variable are n.
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openCnt, closeCnt):
            if openCnt == closeCnt == n:
                res.append("".join(stack))
                return  
            if openCnt < n:
                stack.append('(')
                backtrack(openCnt + 1, closeCnt)
                stack.pop()
            if closeCnt < openCnt:
                stack.append(")")
                backtrack(openCnt, closeCnt + 1)
                stack.pop()
        backtrack(0, 0)
        return res
# @lc code=end

