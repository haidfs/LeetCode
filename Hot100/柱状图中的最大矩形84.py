# 需要注意的是，这里和之前的盛水最多的容器是不一样的，需要用分治法来处理
# 找到最短的短板，然后左右递归 但是分治法也会超时
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
# 通过观察，可以发现，最大面积矩形存在于以下几种情况：
# 1.确定了最矮柱子以后，矩形的宽尽可能往两边延伸。
# 2.在最矮柱子左边的最大面积矩形（子问题）。
# 3.在最矮柱子右边的最大面积矩形（子问题）。
class Solution:
    # 法一，考虑使用分治方法，分治实质上就是多路递归，会超时
    def calculateArea(self, heights: [int], start, end):
        if start > end:
            return 0
        min_index = heights.index(min(heights))
        return max(heights[min_index] * (end - start + 1), max(self.calculateArea(heights, start, min_index - 1),
                                                               self.calculateArea(heights, min_index + 1, end)))

    def largestRectangleArea(self, heights: [int]) -> int:
        return self.calculateArea(heights, 0, len(heights) - 1)

    # 法二，使用栈进行处理
    # 在这种方法中，我们维护一个栈。一开始，我们把 - 1
    # 放进栈的顶部来表示开始。初始化时，按照从左到右的顺序，我们不断将柱子的序号放进栈中，直到遇到相邻柱子呈下降关系，也就是
    # a[i - 1] > a[i]
    # a[i−1] > a[i] 。现在，我们开始将栈中的序号弹出，直到遇到
    # stack[j]
    # stack[j]
    # 满足a\big[stack[j]\big] \leq
    # a[i]
    # a[stack[j]]≤a[i] 。每次我们弹出下标时，我们用弹出元素作为高形成的最大面积矩形的宽是当前元素与
    # stack[top - 1]
    # stack[top−1] 之间的那些柱子。也就是当我们弹出
    # stack[top]
    # stack[top]
    # 时，记当前元素在原数组中的下标为
    # i ，当前弹出元素为高的最大矩形面积为：
    #
    # (i - stack[top - 1] - 1) \times
    # a\big[stack[top]\big].
    # (i−stack[top−1]−1)×a[stack[top]].
    #
    # 更进一步，当我们到达数组的尾部时，我们将栈中剩余元素全部弹出栈。在弹出每一个元素是，我们用下面的式子来求面积： (stack[top] - stack[top - 1]) \times
    # a\big[stack[top]\big](stack[top]−stack[top−1])×a[stack[top]]，其中，stack[top]
    # stack[top]
    # 表示刚刚被弹出的元素。因此，我们可以通过每次比较新计算的矩形面积来获得最大的矩形面积。

    # 构造单调栈的目的就是找到某个柱子能够向右延伸到的最大距离
    def largestRectangleArea2(self, heights: [int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        # 以下代码块代表heights是一个递增数组
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    # 法三：可以考虑使用85题的二进制最大矩阵的动态规划的方法求解，也会超时
    def largestRectangleArea3(self, heights: [int]) -> int:
        if not heights:
            return 0
        rows = max(heights)
        cols = len(heights)
        max_area = 0
        dp = matrix = [[0] * cols for _ in range(rows)]
        col_list = list(range(cols))
        for height, col in zip(heights, col_list):
            for i in range(rows - 1, rows - 1 - height, -1):
                matrix[i][col] = 1
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))
        return max_area


if __name__ == '__main__':
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(s.largestRectangleArea2(heights))