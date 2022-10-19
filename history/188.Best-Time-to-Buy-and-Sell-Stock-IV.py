class Solution(object):
    def maxProfit_k_inf(prices):
        dp_i_0, dp_i_1 = 0, -float('inf')
        for price in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, temp - price)
        return dp_i_0

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        :desc
            给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        :way
            https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/
        """
        lenp = len(prices)
        if k > lenp / 2:
           return maxProfit_k_inf(prices) 
        
        dp = [[[0 for i in range(2)] for _ in range(k + 1)] for _ in range(lenp)]
        print dp
        for i in range(0, lenp):
            for j in range(k, 0, -1):
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j - 1][0] - prices[i])
        return dp[lenp - 1][k][0]

sol = Solution()
prices = [3,2,6,5,0,3]
k = 2
print sol.maxProfit(k, prices)