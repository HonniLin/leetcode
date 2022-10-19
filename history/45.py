'''
@Author: your name
@Date: 2019-10-29 21:14:18
@LastEditTime: 2019-10-29 22:31:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/45.py
题意：给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
链接：https://leetcode-cn.com/problems/jump-game-ii

'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 99999999 
        dp = [99999999 for i in range(len(nums)+1)]
        # for i in range(len(nums)):
        #    dp[i][len(nums)-1] = 0
        for i in range(1, nums[0]+1):
            dp[i] = 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                continue
            for j in range(1, nums[i]+1):
                for k in range(1, len(nums) - j):
                    print i, k+j, dp[j+k] 
                    dp[j+k] = min(dp[j+k], dp[k]+1)
                    print i, j, k, dp[k], j+k, dp[j+k] 
        for i in range(1, len(nums)):
            print i, dp[i]
        ans = dp[len(nums) - 1] 
       
        if ans == 99999999:
            return 0 
        return ans

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    #nums = [1]
    #nums = [2,0,2,0,1]
    nums = [1,1,1,2,1]
    sol = Solution()
    print sol.jump(nums)
