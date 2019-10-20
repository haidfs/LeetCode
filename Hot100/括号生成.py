# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 简单的分析题目，发现这一问题很明显是需要通过递归或者动态规划区处理的。
# 简单分析可以从()往外通过()和"("+")"来递归封装。
# 但是存在一个很明显的问题就是，当n==4时，应该会有这样的一种组合(())(())。但是这种组合通过刚才的方法是得不出来的。
class Solution:
    def __init__(self):
        self.output = []

    def generateParenthesis(self, n: int) -> [str]:
        self.addStr("()", n)
        return sorted(list(set(self.output)))

    def addStr(self, combination, n):
        if n == 1:
            self.output.append(combination)
        else:
            if combination + "()" == "()" + combination:
                self.addStr(combination + "()", n - 1)
            else:
                self.addStr(combination + "()", n - 1)
                self.addStr("()" + combination, n - 1)
            self.addStr("(" + combination + ")", n - 1)

# 方法三，回溯法
# 只有在我们知道序列仍然保持有效的时候才添加"("或者")"。而不是像暴力破解法那样每次都进行添加，我们可以通过
# 跟踪到目前为止放置的左括号和右括号数目来做到这一点
# 如果我们还剩一个位置，我们可以开放一个左括号，如果它不超过左括号的数量，我们可以放置一个右括号
class Solution3(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S + "(", left + 1, right)
            if right < left:
                backtrack(S + ")", left, right + 1)

        backtrack()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    s3 = Solution3()
    print(s3.generateParenthesis(3))