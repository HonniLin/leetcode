'''
@Description: In User Settings Edit
@Author: linhong
@Date: 2019-10-21 20:00:44
@LastEditTime: 2019-10-21 21:12:51
@LastEditors: 
已有的空间可以表示数字。
扫描的时候，当遇到正数，而且这个正数小于数组长度（因为如果大于数组长度，说明前面肯定缺少正数，同时也没有（无需）位置来存储它），
就把它交换到下标和它一样的位置上。这样，扫描完成之后，从1的位置开始判断，如果位置k上存的数字不是k，这就是缺少的第一个正数。
- 数组长度为0，返回 1
- 交换后，游标不移动，继续判断
- 可能从1开始到最后都没有缺少的正数，此时下一个正数可能放在第一个位置上。
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        i = 0
        while i < n:
            if nums[i] > 0 and nums[i] < n and nums[nums[i]] != nums[i]:
                #print i, nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]] 
            else:
                i = i + 1

        #print nums
        for i in range(1, n):
            if i != nums[i]:
                return i
        if nums[0] == n:
            return n + 1
        else:
            return n

if __name__ == "__main__":
    nums = [1, 2, 3]
    nums = [4,3,1,2]
    #nums = [7,8,9,11,12]
    sol = Solution()
    print sol.firstMissingPositive(nums)