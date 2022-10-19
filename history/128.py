class Solution:
    def longestConsecutive(self, nums):
        records = set(nums)
        max_con_len = 0
        for num in nums:
            if num - 1 in records:
                continue
            con_len = 1
            while num + 1 in records:
                num += 1
                con_len += 1
            if con_len > max_con_len:
                max_con_len = con_len
        return max_con_len

sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print sol.longestConsecutive(nums)