'''
@Author: your name
@Date: 2019-12-02 21:35:14
@LastEditTime: 2019-12-02 22:06:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/66.py
desc:
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
链接：https://leetcode-cn.com/problems/plus-one

'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = len(digits)
        cnt = 1
        for i in range(num - 1, -1, -1):
            print i
            if i == num - 1:
                addnum = digits[i] + cnt
                digits[i] = addnum % 10
                cnt = addnum / 10
            elif cnt != 0:
                addnum = digits[i] + cnt
                digits[i] = addnum % 10
                cnt = addnum / 10 

        if cnt != 0:
            tmplist = list()
            tmplist.append(cnt)
            digits = tmplist + digits

        return digits

if __name__ == "__main__":
    sol = Solution()
    digits = [9, 9]
    print sol.plusOne(digits)