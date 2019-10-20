# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from copy import copy
# 递归算法求解全排列
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            temp = map(lambda x: [nums[i]] + x, self.permute(nums[:i] + nums[i + 1:]))
            for n in temp:
                res.append(n)
        return res

    def permute2(self, nums):
        if not nums:
            print(",")
        for i in range(len(nums)):
            print([nums[i]])
            self.permute2(nums[:i] + nums[i + 1:])


class Solution2:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        if len(nums) <= 1:
            return [nums]
        res.append(copy(nums))
        next_permu = self.nextPermutation(copy(nums))
        while next_permu != nums:
            res.append(next_permu)
            next_permu = self.nextPermutation(copy(next_permu))
        return res

    def nextPermutation(self, nums: [int]):
        firstIndex = -1
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        # print(firstIndex)
        if firstIndex == -1:
            reverse(nums, 0, n - 1)
            return copy(nums)
        secondIndex = -1
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex + 1, n - 1)
        return copy(nums)


if __name__ == '__main__':
    arr = [1, 2, 3]
    s = Solution()
    print(s.permute(arr))
    # s.permute2(arr)