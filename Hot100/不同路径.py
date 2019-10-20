# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# https://leetcode-cn.com/problems/unique-paths/
class Solution:
    def __init__(self):
        self.idxs_res = []

    def uniquePaths(self, m: int, n: int) -> int:
        cols = m
        rows = n
        self.idxs_res = [([-1]) * (cols + 1) for _ in range(rows + 1)]
        start_x, start_y = 0, 0
        end_x, end_y = rows - 1, cols - 1
        res = self.helper(start_x, start_y, end_x, end_y)
        return res

    def helper(self, start_x, start_y, end_x, end_y):
        res = 0
        if start_x > end_x or start_y > end_y:
            return 0
        if start_x == end_x and start_y == end_y:
            res = 1
            return res
        if self.idxs_res[start_x + 1][start_y] != -1:
            res += self.idxs_res[start_x + 1][start_y]
        else:
            res += self.helper(start_x + 1, start_y, end_x, end_y)
        if self.idxs_res[start_x][start_y + 1] != -1:
            res += self.idxs_res[start_x][start_y + 1]
        else:
            res += self.helper(start_x, start_y + 1, end_x, end_y)
        self.idxs_res[start_x][start_y] = res
        return res


class Solution2:
    def __init__(self):
        self.res_part = []

    def uniquePaths(self, m: int, n: int) -> int:
        cols = m
        rows = n
        self.res_part = [([-1]) * (cols + 1) for _ in range(rows + 1)]
        end_x, end_y = rows - 1, cols - 1
        for i in range(rows):
            self.res_part[i][end_y] = 1
        for j in range(cols):
            self.res_part[end_x][j] = 1
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                self.res_part[i][j] = self.res_part[i + 1][j] + self.res_part[i][j + 1]
        return self.res_part[0][0]


if __name__ == '__main__':
    s = Solution2()
    print(s.uniquePaths(7, 3))
