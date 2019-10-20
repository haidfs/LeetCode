import sys


# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        rev = sorted(prices, reverse=True)
        if rev == prices:
            return 0
        length = len(prices)
        max_profit = 0
        for i in range(0, length):
            for j in range(i + 1, length):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit

    # 在图表上绘制给定数组中的数字，我们感兴趣的点是图上的峰和谷，需要找到最小的谷之后最大的峰。
    # 我们可以维持两个变量——minprice和maxprofit，它们分别对应迄今为止所得到的最小的谷值和最大的利润（卖出价格与最低价格之间的最大差值）。
    def maxProfit2(self, prices: [int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == '__main__':
    s = Solution()
    arr = [10, 2, 9, 1, 2, 1, 3, 1]
    print(s.maxProfit2(arr))