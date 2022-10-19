'''
@Description: 32. Longest Valid Parentheses
@Author: linhong
@Date: 2019-10-15 20:18:22
@LastEditTime: 2019-10-15 22:18:31
@desc: 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
1/栈记录字符串的下标，进行长度的计算。 list[-1]取栈顶
2/也有dp的做法：
def longestValidParentheses(self, s):
        dp, res = [0] * len(s), 0  # 初始化dp、定义最优结果变量
        for i in range(len(s)):
            if s[i] == ')':  # 只考虑以')'结尾的子串
                if i > 0 and s[i - 1] == '(':  # 第一中情况，直接加 2
                    dp[i] = dp[i - 2] + 2
                if i > 0 and s[i - 1] == ')':  # 第二种情况，
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] - 1 > 0:  # 当前合法子串，前面还有子串，的情况
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:  # 当前合法子串，前面--没有--子串，的情况
                            dp[i] = dp[i - 1] + 2
                res = max(res, dp[i])  # 更新最长的合法子串
        return res
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        medium = [-1]
        ans = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                medium.append(i)
            else:
                medium.pop()
                if not medium:
                    medium.append(i)
                else:
                    #print i, medium[-1] 
                    ans = max(ans, i - medium[-1])

        return ans

if __name__ == "__main__":
    sol = Solution()

    s = "()(()"
    #s = ")()())"
    # s = "()(()"
    # s = "()(()"
    ans = sol.longestValidParentheses(s)
    print ans
