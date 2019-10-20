# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
class Solution:
    def trap(self, height: [int]) -> int:
        length = len(height)
        down, up = None, None
        down_height, up_height = 0, 0
        water = 0
        while True:
            flag = False
            for i in range(1, length):
                if height[i] > height[i - 1] and down is not None:
                    up = i
                    up_height = height[i] - height[i - 1]
                if height[i] < height[i - 1]:
                    down = i - 1
                    down_height = height[i - 1] - height[i]
                if up is not None and down is not None and down < up:
                    flag = True
                    water_height = min(down_height, up_height)
                    water += (up - down - 1) * water_height
                    for index in range(down + 1, up):
                        height[index] += water_height
                    up, down = None, None
            if not flag:
                break
        return water


class Solution2:
    # 参见官方的解法二，两次遍历扫出来左边的最大值数组和右边的最大值数组，取最小减去高度再累加即可
    def trap(self, height: [int]) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max, right_max = [0 for _ in range(size)], [0 for _ in range(size)]
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2]
    print(s.trap(nums))