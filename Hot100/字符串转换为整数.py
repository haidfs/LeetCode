import re


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s_process = s.strip()
        if not s_process:
            return 0
        if re.match(r"^(\-|\+)?\d+", s_process):
            for i in range(1, len(s_process)):
                if not re.match(r"\d", s_process[i]):
                    s_process = s_process[:i]
                    break
            num = int(s_process)
            if num < pow(-2, 31):
                return pow(-2, 31)
            if num >= pow(2, 31):
                return pow(2, 31) - 1
            return num
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("4193 with words"))