'''
@Author: your name
@Date: 2020-02-15 22:19:30
@LastEditTime : 2020-02-15 23:04:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/91.py
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]

sol = Solution()
s = "12"
print sol.numDecodings(s)