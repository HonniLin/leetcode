'''
@Author: your name
@Date: 2019-12-11 21:50:20
@LastEditTime: 2019-12-11 22:28:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/71.py
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        plen = len(path)
        st = list()
        i = 0
        while i < plen:
            if path[i] != '/':
                tmp = ""
                while (i < plen and path[i] != '/'):
                    tmp = tmp + path[i]
                    i = i + 1
                if tmp == "..":
                    if len(st) != 0:
                        st.pop()
                elif tmp != ".":
                    st.append(tmp)
                i = i + 1
            else:
                i = i + 1
        res = "/"
        for i in range(len(st)):
            res = res + st[i]
            if i != len(st)-1:
                res = res + '/'
        return res

sol = Solution()
path = "/a/../../b/../c//.//" 
path = "/a//b////c/d//././/.."
#path = "/home//foo/"
#path = "/../"
print sol.simplifyPath(path)