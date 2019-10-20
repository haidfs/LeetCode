# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # 简单的画图就知道 这里明显是树型结构，所有的树型结构一定会用到递归，这一般还会和变长类型的结果出现在一起
        # 这里的for循环肯定是不通的，能够想到要递归处理，但是要如何递归，却没有明确思路
        output = []

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        if digits:
            backtrack("", digits)
        return output


class Solution2:
    def __init__(self):
        self.output = []
        self.phone = {"2": 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:

        if digits:
            self.backtrack("", digits)
        return self.output

    def backtrack(self, combination, next_digits):
        if len(next_digits) == 0:
            self.output.append(combination)
        else:
            for letter in self.phone[next_digits[0]]:
                self.backtrack(combination + letter, next_digits[1:])


if __name__ == '__main__':
    s = Solution()
    str = "23"
    print(s.letterCombinations(str))