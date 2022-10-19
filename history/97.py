'''
@Author: your name
@Date: 2020-02-23 20:46:09
@LastEditTime : 2020-02-23 21:06:06
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/97.py
两个字符串看成2维地图
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False
        dp = [[False for i in range(len2 + 1)] for j in range(len1 + 1)]
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1] == s3[j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s3[i - 1])
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len1][len2]

sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbbbaccc"
print sol.isInterleave(s1, s2, s3)