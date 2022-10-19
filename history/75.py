# coding=utf8
'''
@Author: your name
@Date: 2019-12-24 21:16:33
@LastEditTime: 2019-12-24 21:24:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/75.py
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = [0 for i in range(3)]
        for i in range(len(nums)):
            cnt[nums[i]] = cnt[nums[i]] + 1
        
        ti = 0
        for i in range(3):
            j = 0
            while j < cnt[i]:
                nums[ti] = i
                ti = ti + 1
                j = j + 1
        
        return nums

    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

sol = Solution()
nums = [2,0,2,1,1,0]
print sol.sortColors(nums)
            
