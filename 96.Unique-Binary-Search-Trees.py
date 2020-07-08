# -*- encoding: utf-8 -*-
'''
@File    :   96.Unique-Binary-Search-Trees.py
@Time    :   2020/07/08 11:44:12
@Author  :   yourname 
@Desc    :   
'''

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        :desc n个节点能组成多少不同的二叉搜索树`
        :way 卡特兰数
        G(n): 长度为n的序列的不同二叉搜索树个数。
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]