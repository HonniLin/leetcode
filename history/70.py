'''
@Author: your name
@Date: 2019-12-10 22:04:04
@LastEditTime: 2019-12-10 22:14:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/70.py
入门dp题
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        
        if n < 2:
            return dp[n]
        dp[0] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
sol = Solution()
print sol.climbStairs(2)