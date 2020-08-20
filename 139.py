#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   139.py
@Time    :   2020/04/07 22:29:18
@Author  :   linhong02
@Desc    :   
玩子数组或者子字符串且求极值的题，基本就是 DP 没差了，虽然这道题没有求极值，但是玩子字符串也符合 DP 的状态转移的特点。
用j把 [0, i) 范围内的子串分为了两部分，[0, j) 和 [j, i)，其中范围 [0, j) 就是 dp[j]，范围 [j, i) 就是 s.substr(j, i-j)，
其中 dp[j] 是之前的状态，我们已经算出来了，可以直接取，只需要在字典中查找 s.substr(j, i-j) 是否存在了，如果二者均为 true，将 dp[i] 赋为 true，
并且 break 掉
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            print i
            for j in range(0, i):
                #print s[:j], s[j:i], j
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
#s = "applepenapple"
#wordDict = ["apple", "pen"]
#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]
#s = "a"
#wordDict = ["a"]
sol = Solution()
print sol.wordBreak(s, wordDict)

