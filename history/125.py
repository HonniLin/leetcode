#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   125.py
@Time    :   2020/03/15 18:47:20
@Author  :   linhong02
@Desc    :   将用s.lower()将字母转为小写，i.isalnum()判断字符变量c是否为字母或数字
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == []:
            return True
        new_s = [i for i in s.lower() if i.isalnum()]
        return new_s == new_s[::-1]