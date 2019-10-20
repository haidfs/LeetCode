# 猜测结果为catalan数，其公式为C n =C(2n,n)/(n+1)
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
from functools import reduce


def numTrees(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    a = reduce(lambda x, y: x * y, list(range(n + 2, 2 * n + 1)))
    b = reduce(lambda x, y: x * y, list(range(1, n + 1)))
    return a // b


class Solution(object):
    def numTrees(self, n):
        # 动态规划求解此问题
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    print(numTrees(3))