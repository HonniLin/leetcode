#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   30.py
@Time    :   2020/05/17 14:18:10
@Author  :   linhong02
@Desc    :   None
"""

'''
@Description: 30. Substring with Concatenation of All Words
                给定一个长字符串，再给定几个长度相同的单词，找出串联给定所有单词的子串的起始位置。
@Author: linhong02
@Date: 2019-09-22 18:14:17
@LastEditTime: 2019-09-22 19:12:08
@LastEditors: 
使用一个字典统计一下L中每个单词的数量。由于每个单词的长度一样，以题中给的例子而言，可以3个字母3个字母的检查，如果不在字典中，则break出循环。有一个技巧是建立一个临时字典curr，用来统计S中那些在L中的单词的数量，必须和L中单词的数量相等，否则同样break。
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if len(s) == 0 or len(words) == 0:
            return res
        words_len = len(words)
        words_dict = dict()
        for i in words:
            if i in words_dict:
                words_dict[i] = words_dict[i] + 1
            else:
                words_dict[i] = 1
        #print "***", words_dict
        wlen = len(words[0])
        for i in range(len(s) + 1 - words_len * wlen):
            j = 0
            curr = dict()
            while j < words_len:
                word = s[i + j * wlen : i + j * wlen + wlen]
                #print "**", word
                if word not in words_dict:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] = curr[word] + 1
                if curr[word] > words_dict[word]:
                    break
                j = j + 1
            if j == words_len:
                res.append(i)
        return res

if __name__ == "__main__":
    sol = Solution()
    #s = "barfoothefoobarman"
    #words = ["foo","bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    res = sol.findSubstring(s, words)
    print res