'''
@Author: your name
@Date: 2020-02-16 21:11:15
@LastEditTime : 2020-02-16 21:29:13
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/93.py
dfs
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, sub, ips, ip):
            if sub == 4:
                if s == '':
                    ips.append(ip[1:])
                return
            for i in range(1, 4):
                if len(s) >= i:
                    if int(s[:i]) < 256:
                        dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                    if s[0] == '0':
                        break
        ips = []
        dfs(s, 0, ips, '')
        return ips
sol = Solution()
s = '00000'
print sol.restoreIpAddresses(s)
