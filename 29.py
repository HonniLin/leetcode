'''
@Description: In User Settings Edit
@Author: linhong
@Date: 2019-09-15 17:20:53
@LastEditTime: 2019-09-15 17:47:19
@LastEditors: Please set LastEditors
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        str_dividend = ""
        
        flag = 1
        if dividend < 0 and divisor > 0:
            flag = -1
            dividend = dividend * -1
        elif dividend > 0 and divisor < 0:
            flag = -1
            divisor = divisor * -1
        elif dividend < 0 and divisor < 0:
            dividend = dividend * -1
            divisor = divisor * -1

        if dividend < divisor:
            return 0

        while dividend > 0:
            str_dividend = str_dividend + str(dividend % 10)
            dividend = dividend / 10
        
        leng = len(str_dividend)
        tmp = 0
        ans = 0
        #print str_dividend 
        for i in range(leng - 1, -1, -1):
            tmp = tmp * 10 + int(str_dividend[i])
            if tmp >= divisor:
                #print tmp
                ans = ans * 10 + tmp / divisor
                tmp = tmp % divisor
            else:
                ans = ans * 10
        ans = ans * flag
        return ans if -2**31<=ans<=2**31-1 else 2**31-1

if __name__ == "__main__":
    sol = Solution()
    print sol.divide(-2147483648, -1)

    
                
            
