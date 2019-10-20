class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归解法是可行的，但是很明显的时间复杂度会很高
        if not s and not p:
            return True
        if s and not p:
            return False
        if len(p) > 1 and p[1] == "*":
            if s and (s[0] == p[0] or p[0] == "."):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        else:
            if s and (s[0] == p[0] or p[0] == "."):
                return self.isMatch(s[1:], p[1:])
        return False


if __name__ == '__main__':
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"
    so = Solution()
    print(so.isMatch(s, p))