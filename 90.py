'''
@Author: your name
@Date: 2020-02-12 21:17:48
@LastEditTime : 2020-02-12 21:38:06
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/90.py
排序，dfs
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = list()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i  > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, res, path + [nums[i]])

sol = Solution()
nums = [1, 2, 2]
print sol.subsetsWithDup(nums)