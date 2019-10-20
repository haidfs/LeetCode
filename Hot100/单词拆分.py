# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# 自己理解的动态规划，很明显的会有一定的问题
# 这种反向的动规，没有实际的意义，和正向的递归是一样的
# 在
class Solution:
    # 递归的套路 基本都是for if递归return True,for循环结束后returnFALSE。
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        if not s:
            return True
        for i in wordDict:
            if s.startswith(i):
                if self.wordBreak(s[len(i):], wordDict):
                    return True
        return False


# 这一种方法与solution的基本思路是一样的，这两个的区别在于第一种方法一旦匹配上之后，后续的单词不匹配的话没有回溯，
# 而是直接返回False，第二种如果不匹配。还会继续回溯检查别的选项，直到所有的都遍历完成，都不匹配，才会返回False。
class Solution2:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        return self.word_break(s, list(set(wordDict)), 0)

    def word_break(self, s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.word_break(s, wordDict, end):
                return True
        return False


# 方法三：记忆化回溯
class Solution3:
    def __init__(self):
        self.memo = []

    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        self.memo = [2 for i in range(len(s))]
        return self.word_break(s, list(set(wordDict)), 0)

    def word_break(self, s, wordDict, start):
        if start == len(s):
            return True
        if self.memo[start] != 2:
            return self.memo[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.word_break(s, wordDict, end):
                self.memo[start] = True
                return True
        self.memo[start] = False
        return False


# 方法三，动态规划
class Solution4:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        wordDict = list(set(wordDict))
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    s = Solution()
    test_str = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
    wordDict = ['aaa']
    # print(len(wordDict))
    print(s.wordBreak(test_str, wordDict))