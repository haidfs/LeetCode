import math

# “若向内移动短板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
# 若向内移动长板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 不变或变小，下个水槽的面积一定小于当前水槽面积。“其实可以加一句，无论是移动短板或者长板，
# 我们都只关注移动后的新短板会不会变长，而每次移动的木板都只有三种情况，
# 比原短板短，比原短板长，与原短板相等；如向内移动长板，对于新的木板：1.比原短板短，则新短板更短。2.与原短板相等或者比原短板长，则新短板不变。
# 所以，向内移动长板，一定不能使新短板变长。
class Solution:
    # 暴力破解法超时
    def maxArea(self, height: [int]) -> int:
        length = len(height)
        if length < 2:
            return 0
        max_area = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea2(self, height: [int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height))
