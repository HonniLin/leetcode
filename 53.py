'''
@Author: your name
@Date: 2019-10-30 20:27:02
@LastEditTime: 2019-10-30 20:30:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/53.py
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        res = 0
        for i in range(len(nums)):
            res = res + nums[i]
            ans = max(ans, res)
            if res < 0:
                res = 0

        return ans

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-1]
    sol = Solution()
    print sol.maxSubArray(nums)