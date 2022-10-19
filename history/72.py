'''
@Author: your name
@Date: 2019-12-16 22:44:57
@LastEditTime: 2019-12-16 23:05:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/72.py
定义dp[i][j]为word1中前ii个字符组成的串，与word2中前jj个字符组成的串的编辑距离。

插入操作：在word1的前ii个字符后插入一个字符，使得插入的字符等于新加入的word2[j]。
这里要考虑清楚，插入操作对于原word1字符来说，ii是没有前进的，而对于word2来说是前进了一位然后两个字符串才相等的。
所以此时是dp[i][j]=dp[i][j-1]+1。

删除操作：在word1的第i−1i−1​个字符后删除一个字符，使得删除后的字符串word[:i-1]与word2[:j]相同。
这里要考虑清楚，删除操作对于原word2字符来说，j−1j−1​是没有前进的，而对于word1来说是删除了一位然后两个字符串才相等的。
所以此时是dp[i][j]=dp[i-1][j]+(0 or 1)。
————————————————
原文链接：https://blog.csdn.net/iyuanshuo/article/details/80112211
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        dp = [[0 for i in range(len2)] for j in range(len1)]
        for i in range(len1):
            dp[i][0] = i
        for i in range(len2):
            dp[0][i] = i
        
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[len1-1][len2-1]

sol = Solution()
word1 = "horse"
word2 = "ros"
print sol.minDistance(word1, word2)


