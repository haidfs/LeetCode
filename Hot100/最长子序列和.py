# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums: [int]):
        # 利用给出的测试例进行简单的分析。
        temp = nums[0]
        max_ = temp
        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]
                max_ = max(max_, temp)

            else:
                temp = nums[i]
                max_ = max(max_, temp)
        return max_

    def maxSubArray2(self, nums: [int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_


if __name__ == '__main__':
    s = Solution()
    arr = [8, -19, 5, -4, 20]
    print(s.maxSubArray(arr))