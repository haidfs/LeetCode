# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小
# 这道题没有太多好说的，比较简单的动态规划，直接递推即可
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = [([-1]) * cols for _ in range(rows)]
        res[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
        for i in range(rows - 2, -1, -1):
            res[i][cols - 1] = grid[i][cols - 1] + res[i + 1][cols - 1]
        for j in range(cols - 2, -1, -1):
            res[rows - 1][j] = grid[rows - 1][j] + res[rows - 1][j + 1]
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                res[i][j] = min(grid[i][j] + res[i + 1][j], grid[i][j] + res[i][j + 1])
        return res[0][0]


if __name__ == '__main__':
    arr = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution()
    print(s.minPathSum(arr))