# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
# 法1：暴力破解法，后续测试用例会超时
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0 or length == 1:
            return s
        max_palin = ""
        max_length = 0
        for i in range(length):
            for j in range(i + 1, length + 1):
                if s[i:j] == s[i:j][::-1] and (j - i) >= max_length:
                    max_palin = s[i:j]
                    max_length = j - i
                # else:
                #     break
        return max_palin


# 法二：中心扩展法
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if not s or length == 1:
            return s
        start, end = 0, 0
        for i in range(length):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                start = i - (max_len - 1) / 2
                end = i + max_len / 2
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


# 法三：动态规划法
# dp[i][i]=1; //单个字符是回文串
# dp[i][i+1]=1 if s[i]=s[i+1]; //连续两个相同字符是回文串
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0 or length == 1:
            return s
        start, max = 0, 1
        dp = [([0]) * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
            if i < length - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max = 2
                start = i
        for l in range(3, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    start = i
                    max = l
        return s[start:start + max]


if __name__ == '__main__':
    test = "aaa"
