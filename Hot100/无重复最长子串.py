# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_sub_lenth = 1
        length = len(s)
        for i in range(length - 1):
            non_repeat = s[i]
            for j in range(i + 1, length):
                if s[j] not in non_repeat:
                    non_repeat += s[j]
                else:
                    if len(non_repeat) > max_sub_lenth:
                        max_sub_lenth = len(non_repeat)
                    break
            # 检测从头到尾都没有重复字符出现的情况
            if len(non_repeat) > max_sub_lenth:
                max_sub_lenth = len(non_repeat)
        return max_sub_lenth


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("au"))