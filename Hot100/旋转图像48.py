# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
class Solution:
    def rotate(self, matrix: [[int]]) -> [[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for j in range(cols):
            res_part = []
            for i in range(rows - 1, -1, -1):
                res_part.append(matrix[i][j])
            res.append(res_part)
        return res
    # 先翻转再转置
    def rotate2(self, matrix: [[int]]) -> [int]:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows <= 1:
            return matrix
        if rows % 2 == 0:
            for i in range(rows // 2, rows):
                matrix[i], matrix[rows - 1 - i] = matrix[rows - 1 - i], matrix[i]
        else:
            for i in range(rows // 2 + 1, rows):
                matrix[i], matrix[rows - 1 - i] = matrix[rows - 1 - i], matrix[i]
        for i in range(rows):
            for j in range(i, cols):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2],
        [3, 4]
    ]
    print(s.rotate2(matrix))