# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# # 输出: 6
# 我们可以以常数时间计算出在给定的坐标结束的矩形的最大宽度。我们可以通过记录每一行中每一个方块连续的“1”的数量来实现这一点。每遍历完一行，
# 就更新该点的最大可能宽度。
# 每个点对应的最大宽度，我们就可以在线性时间内计算出以该点为右下角的最大矩形。当我们遍历列时，可知从初始点到当前点矩形的最大宽度，就是我们遇到的每个最大宽度的最小值。


class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        max_area = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))
        return max_area


if __name__ == '__main__':
    s = Solution()
    arr = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    print(s.maximalRectangle(arr))