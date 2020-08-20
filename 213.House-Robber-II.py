class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :desc 类比 198，但数组为环形数组
        :way 空间复杂度·O(1)
        """
        def work(nums):
            cur, pre = 0, 0
            for i in range(len(nums)):
                cur, pre = max(pre + nums[i], cur), cur
            return cur
        return max(work(nums[:-1]), work(nums[1:])) if len(nums) != 1 else nums[0]

sol = Solution()
nums = [2,3,2]
print sol.rob(nums)