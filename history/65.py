'''
@Author: your name
@Date: 2019-12-03 21:19:02
@LastEditTime: 2019-12-03 21:23:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/65.py
枚举各种情况
'''
#submit
class Solution:
    def isNumber(self, s):
        num = False; numAfterE = True; dot = False; exp = False; sign = False; length =len(s)
        for i in range(length):
            if s[i] == ' ':
                if i < length - 1 and s[i + 1] != ' ' and (num or dot or exp or sign):  return False
            elif s[i] in {'+', '-'}:
                if i > 0 and s[i - 1] not in {' ', 'e'}: return False
                sign = True
            elif s[i] >= '0' and s[i] <= '9':
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp: return False
                dot = True
            elif s[i] == 'e':
                if exp or not num: return False
                exp = True
                numAfterE = False
            else: return False
        return num and numAfterE

print(Solution().isNumber(" 005047e+6")) 
