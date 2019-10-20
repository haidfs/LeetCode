# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0

    def exist(self, board: [[str]], word: str) -> bool:
        if not board or not bool:
            return False
        self.rows = len(board)
        self.cols = len(board[0])
        visited = [([False]) * self.cols for _ in range(self.rows)]
        word_length = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.exist_helper(board, i, j, visited, word_length, word):
                    return True
        return False

    def exist_helper(self, board, row, col, visited, word_length, word):
        if word_length == len(word):
            return True
        exit_word = False
        if 0 <= row < self.rows and 0 <= col < self.cols and not visited[row][col] and board[row][col] == word[
            word_length]:
            visited[row][col] = True
            word_length += 1
            exit_word = self.exist_helper(board, row - 1, col, visited, word_length, word) or \
                        self.exist_helper(board, row, col - 1, visited, word_length, word) or \
                        self.exist_helper(board, row + 1, col, visited, word_length, word) or \
                        self.exist_helper(board, row, col + 1, visited, word_length, word)
            if not exit_word:
                word_length -= 1
                visited[row][col] = False
        return exit_word