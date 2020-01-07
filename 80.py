'''
@Author: your name
@Date: 2020-01-07 21:52:45
@LastEditTime: 2020-01-07 22:21:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/80.py
用一个变量计数和记录当前值
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        num = nums[0]
        cnt = 1
        ans = 1
        for i in range(1, len(nums)):
            if num != nums[i]:
                cnt = 1
                num = nums[i]
                nums[ans] = num
                ans = ans + 1
            elif num == nums[i] and cnt < 2:
                cnt = cnt + 1
                nums[ans] = num
                ans = ans + 1
        nums = nums[:ans]
        return ans

sol = Solution()
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
print sol.removeDuplicates(nums)