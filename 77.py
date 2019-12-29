'''
@Author: your name
@Date: 2019-12-24 21:28:38
@LastEditTime: 2019-12-24 22:40:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/76.py
dfs
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        ans = []
        self.count = 0

        def dfs(start, valuelist):
            if self.count == k:
                ans.append(valuelist)
                return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1

        dfs(1, [])
        return ans
        
sol = Solution()
n = 4
k = 2
print sol.combine(n, k)