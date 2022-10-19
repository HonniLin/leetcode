#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (42.99%)
# Likes:    3238
# Dislikes: 644
# Total Accepted:    432.6K
# Total Submissions: 1M
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
# 
# Note that division between two integers should truncate toward zero.
# 
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
# 
# 
# Example 1:
# 
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#

# @lc code=start
class Solution:
    # I used stack to solve the problem.
    # As you can see, I add every token as an integer in the stack, unless it's an operation
    # In that case, I pop two elements from the stack and then save the result back to it. 
    # After all operations are done through, the remaining element in the stack will be the result.
    def calculator(self, a: int, b: int, ope: str) -> int:
        if ope == '+':
            return a + b
        if ope == '-':
            return a - b
        if ope == '*':
            return a * b
        if ope == '/':
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/'] 
        numStack = []
        res = 0
        for s in tokens:
            if s in operators:
                b = numStack.pop()
                a = numStack.pop()
                equ = self.calculator(a, b, s)
                numStack.append(equ)
            else:
                numStack.append(int(s))
        return numStack[0]

# @lc code=end

