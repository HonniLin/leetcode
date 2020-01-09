# coding=utf-8
'''
@Author: your name
@Date: 2020-01-09 20:44:35
@LastEditTime: 2020-01-09 21:23:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/81.py
加了一个可能含有重复数字。
这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，先移动左指针，是他指向一个和右指针不同的数字上。

只在有序的一边查找：
至于查找部分，可以这么考虑：首先nums[l] > num[r]认为是恒成立的。
如果mid指向的位置比nums[l]还大，那么说明l到mid是有序的，这个时候如果nums[l] <= target < nums[mid]说明要查找的在Mid前面，移动右指针；否则要查找的在mid后面，移动左指针。
如果mid指向的位置比nums[r]还小，那么说明mid到r是有序的，然后同样的进行比较操作就行了。
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left = left + 1
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        
sol = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print sol.search(nums, target)