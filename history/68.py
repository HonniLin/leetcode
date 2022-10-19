'''
@Author: your name
@Date: 2019-12-09 20:54:56
@LastEditTime: 2019-12-09 21:57:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/68.py
没啥难度，主要的处理在空格的平均分配上。
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        wnum = len(words)
        res = list()
        ws = 0
        st = 0
        i = 0
        while i < wnum:
            ws = ws + len(words[i])
            cnt = i - st
            if ws + cnt > maxWidth:
                cnt = cnt - 1
                s = ""
                ed = i
                ws = ws - len(words[i])
                kong = maxWidth - ws
                if cnt != 0:
                    firstkong = kong % cnt
                    avgkong = kong / cnt
                else:
                    firstkong = kong
                
                for j in range(st, ed):
                    if j == ed - 1:
                        s = s + words[j]
                    elif firstkong > 0:
                        s = s + words[j] + ' ' * (avgkong + 1)
                        firstkong = firstkong - 1
                    elif firstkong == 0:
                        s = s + words[j] + ' ' * avgkong
                #print s
                if firstkong != 0:
                    s = s + ' ' * firstkong
                res.append(s)
                ws = len(words[i])
                st = i
                cnt = 0
                i = i + 1
            else:
                i = i + 1
        s = ""
        for i in range(st, wnum):
            s = s + words[i]
            if i < wnum - 1:
                s = s + ' '
            else:
                maxWidth = maxWidth - len(s)
                s = s + ' ' * maxWidth
        res.append(s)

        return res

sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
#words = ["What","must","be","acknowledgment","shall","be"]
#maxWidth = 16
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
#words = ["Science","is","what","we","understand","well","enough","to","explain",
#         "to","a","computer.","Art","is","everything","else","we","do"]
#maxWidth = 20
print sol.fullJustify(words, maxWidth)