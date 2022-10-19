'''
@Author: your name
@Date: 2019-11-13 21:28:27
@LastEditTime: 2019-11-13 22:31:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/54.py
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = list()
        if matrix == []:
            return res
        mlen = len(matrix) #hang
        nlen = len(matrix[0]) #lie
        
        lm = 0
        rm = mlen - 1
        ln = 0
        rn = nlen - 1
        while lm <= rm and ln <= rn:
            #print lm, rm, ln, rn
            for i in range(ln, rn+1):
                res.append(matrix[lm][i])
            #print "1", res
            for i in range(lm+1, rm+1):
                res.append(matrix[i][rn])
            #print "2", res
            for i in range(rn-1, ln-1, -1):
                if lm < rm:
                    res.append(matrix[rm][i])
            #print "3", res
            for i in range(rm-1, lm, -1):
                if ln < rn:
                    res.append(matrix[i][ln])
            #print "4", res
            lm = lm + 1
            rm = rm - 1
            ln = ln + 1
            rn = rn - 1
        
        return res

if __name__ == "__main__":
    matrix = [
  [1, 2, 3, 4],
  [9,10,11,12]
]
    sol = Solution()
    print sol.spiralOrder(matrix)