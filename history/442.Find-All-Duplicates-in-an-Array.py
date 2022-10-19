class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :desc: Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
               Find all the elements that appear twice in this array.
        :way:
        借用索引号，因为是在1~n之间，那么我们可以用索引0表示数字1，索引1表示数字2...，
        当有个数字num，我们将num - 1的位置的数字取相反数，连续两次取相反数会变回来，便可判断元素出现次数。
        所以时间复杂度为O(n)O(n)
        """
        res = []
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            if nums[loc] < 0:
                res.append(loc + 1)
            nums[loc] = -nums[loc]
        return res