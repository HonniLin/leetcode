#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   140.Word-Break-II.py
@Time    :   2020/06/30 23:33:04
@Author  :   linhong02
@Desc    :   
记忆化的方法，我们使用一个 key:valuekey:value 这样的哈希表来进行优化。
在哈希表中， keykey 是当前考虑字符串的开始下标， valuevalue 包含了所有从头开始的所有可行句子。
下次我们遇到相同位置开始的调用时，我们可以直接从哈希表里返回结果，而不需要重新计算结果。

通过记忆化的方法，许多冗余的子问题都可以被省去，回溯树得到了剪枝，所以极大程度降低了时间复杂度。
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)
    
    def dfs(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            tmp =  self.dfs(s[len(word):], res, wordDict, memo)
            print tmp
            for r in tmp:
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        print memo
        return res

sol = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print sol.wordBreak(s, wordDict)