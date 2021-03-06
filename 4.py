#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   4.py
@Time    :   2020/05/02 16:21:29
@Author  :   linhong02
@Desc    :   
             mid
...nums1[i-1] | nums1[i]...
...nums2[j-1] | nums2[j]...

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            return ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and nums1[i] < nums2[j - 1]:
                # i 小了
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i 大了
                imax = i - 1
            else:
                if i == 0: max_left = nums2[j - 1]
                elif j == 0: max_left = nums1[i - 1]
                else: max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left
                
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0

sol = Solution()
nums1 = [1, 3]
nums2 = [2]
print sol.findMedianSortedArrays(nums1, nums2)