#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   322.py
@Time    :   2020/03/29 17:27:47
@Author  :   linhong02
@Desc    :   凑硬币
dp 假设dp[i]表示凑够i元所需要的最少硬币数，一共有n种面值硬币，那么dp[i]=min(dp[i−coins[0]],dp[i−coins[1]],...dp[i−coins[k])+1，其中coins[k]<=i
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins_num = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(coins_num):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

sol = Solution()
coins = [5]
amount = 11
print sol.coinChange(coins, amount)


        