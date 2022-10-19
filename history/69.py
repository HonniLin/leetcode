# coding=utf8
'''
@Author: your name
@Date: 2019-12-10 21:34:57
@LastEditTime: 2019-12-10 21:55:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/69.py
x 的平方根，二分
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        res = 1
        left, right = 0, x
        while abs(res - x) > 0.000001:
            mid = left + (float(right - left))/ 2
            res = mid * mid
            if res < x:
                left = mid
            else:
                right = mid
        return int(mid)

sol = Solution()
print sol.mySqrt(9)