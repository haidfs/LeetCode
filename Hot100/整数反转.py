class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s.startswith("-"):
            s = s[1:]
            res = -(int(s[::-1]))
        else:
            res = int(s[::-1])
        if res < pow(-2, 31) or res > pow(2, 31) - 1:
            return 0
        return res