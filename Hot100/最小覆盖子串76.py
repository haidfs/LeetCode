# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
from collections import Counter


class Solution:
    # 这道题目是用滑动窗口来求解的
    # 滑动窗口基本上都是双指针进行处理，lr先都置为0，当r右移到一个可行解的时候，开始左移左指针。左指针一直保持
    # 可行解时，记录对应的窗口索引。左指针不能保持可行解时，右移右指针。

    # 上面这么处理是可以解决问题的，但是还存在着优化的空间。即当S中存在着大量T中没有的字符时，可以先做一步filter操作。
    # 再在filter字符上面进行处理、
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        filter_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filter_s.append((i, char))
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(filter_s):
            character = filter_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            if window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = filter_s[l][1]

                end = filter_s[r][0]
                start = filter_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    S = "a"
    T = "a"
    s = Solution()
    print(s.minWindow(S, T))