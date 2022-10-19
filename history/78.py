'''
@Author: your name
@Date: 2020-01-02 22:40:24
@LastEditTime: 2020-01-02 22:46:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/78.py
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lens = len(nums)
        temp = list()
        res = list()
        def dfs(temp, res, start):
            x = temp[:]
            res.append(x)
            for i in range(start, lens):
                temp.append(nums[i])
                dfs(temp, res, i+1)
                temp.pop()
        dfs(temp, res, 0)
        return res

sol = Solution()
nums = [1, 2, 3]
print sol.subsets(nums)
