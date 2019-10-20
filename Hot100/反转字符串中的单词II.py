class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(map(lambda x: self.reverse_word(x), s.split()))
        return " ".join(s)

    def reverse_word(self, s):
        n = len(s)
        if n % 2 == 0:
            end_index = n // 2
        else:
            end_index = n // 2 + 1
        s = list(s)
        for i in range(end_index):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        s = "".join(s)
        return s


if __name__ == '__main__':
    str1 = "Let's take LeetCode contest"
    s = Solution()
    print(s.reverseWords(str1))