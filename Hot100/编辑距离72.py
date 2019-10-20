# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')

# 动态规划的第一步肯定是确定状态空间的跳转，一般来说，两个字符串的问题，状态空间都是在一个二维数组里面进行跳转dp[i][j]
# 需要明确子结构，推出递归表达式
#
# dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数
# 所以，
# 当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；
# 当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# 其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return n + m
        d = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        return d[n][m]


if __name__ == '__main__':
    s1 = "horse"
    s2 = "ros"
    s = Solution()
    print(s.minDistance(s1, s2))