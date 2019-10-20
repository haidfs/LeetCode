# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1:
            return s
        numCols, rebuild_flags = self.getColsAndFlags(length, numRows)
        myList = [(["##"]) * numCols for i in range(numRows)]
        cur = 0
        for j in range(numCols):
            if rebuild_flags[j]:
                for i in range(numRows):
                    if cur < length:
                        myList[i][j] = s[cur]
                        cur += 1
                    else:
                        break
            else:
                myList[i - 1][j] = s[cur]
                i -= 1
                cur += 1
        res = ""
        for i in range(numRows):
            for j in range(numCols):
                if myList[i][j] != "##":
                    res += myList[i][j]
        return res

    def getColsAndFlags(self, length, numRows):
        mid_cols = numRows - 2
        num_cols = 0
        rebuild_flag = []
        while length >= 0:
            if length <= 0:
                break
            length -= numRows
            num_cols += 1
            rebuild_flag.append(True)
            for _ in range(mid_cols):
                if length <= 0:
                    break
                length -= 1
                num_cols += 1
                rebuild_flag.append(False)
        return num_cols, rebuild_flag


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row].append(c)
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = (going_down != True)
            cur_row += 1 if going_down else -1
        res = []
        for row in rows:
            res.extend(row)
        res = "".join(res)
        return res


if __name__ == '__main__':
    s = Solution2()
    print(s.convert("PAYPALISHIRING", 4))# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows == 1:
            return s
        numCols, rebuild_flags = self.getColsAndFlags(length, numRows)
        myList = [(["##"]) * numCols for i in range(numRows)]
        cur = 0
        for j in range(numCols):
            if rebuild_flags[j]:
                for i in range(numRows):
                    if cur < length:
                        myList[i][j] = s[cur]
                        cur += 1
                    else:
                        break
            else:
                myList[i - 1][j] = s[cur]
                i -= 1
                cur += 1
        res = ""
        for i in range(numRows):
            for j in range(numCols):
                if myList[i][j] != "##":
                    res += myList[i][j]
        return res

    def getColsAndFlags(self, length, numRows):
        mid_cols = numRows - 2
        num_cols = 0
        rebuild_flag = []
        while length >= 0:
            if length <= 0:
                break
            length -= numRows
            num_cols += 1
            rebuild_flag.append(True)
            for _ in range(mid_cols):
                if length <= 0:
                    break
                length -= 1
                num_cols += 1
                rebuild_flag.append(False)
        return num_cols, rebuild_flag


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row].append(c)
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = (going_down != True)
            cur_row += 1 if going_down else -1
        res = []
        for row in rows:
            res.extend(row)
        res = "".join(res)
        return res


if __name__ == '__main__':
    s = Solution2()
    print(s.convert("PAYPALISHIRING", 4))