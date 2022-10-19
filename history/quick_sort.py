#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   quick_sort.py
@Time    :   2020/07/16 15:09:27
@Author  :   linhong02
@Desc    :   快排
"""
def quick_sort(nums, start, end):
    """
    :desc 递归
    """
    if start >= end:
        return

    left = start
    right = end
    mid = nums[left]
    while left < right:
        while left < right and nums[right] >= mid:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < mid:
            left += 1
        nums[right] = nums[left]
    nums[left] = mid
    quick_sort(nums, start, left - 1)
    quick_sort(nums, left + 1, end)

def quick_sort_2(nums, start, end):
    """
    非递归
    """
    def partition(nums, l, r):
        mid = nums[l]
        while l < r:
            while l < r and nums[r] >= mid:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] < mid:
                l += 1
            nums[r] = nums[l]
        nums[l] = mid
        return l

    if len(nums) < 2:
        return nums
    stack = []
    stack.append(end)
    stack.append(start)
    while stack:
        left = stack.pop()
        right = stack.pop()
        index = partition(nums, left, right)
        if index < right:
            stack.append(right)
            stack.append(index + 1)
        if index > left:
            stack.append(index - 1)
            stack.append(left)



nums = [2, 1, 3, 4, 1]
quick_sort_2(nums, 0, len(nums) - 1)
print nums
quick_sort(nums, 0, len(nums) - 1)
print nums
