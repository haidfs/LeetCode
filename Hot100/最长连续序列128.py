# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4
from collections import defaultdict


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        length = len(nums)
        max_sub = 1
        temp_sub = 1
        for i in range(length - 1):
            if nums[i + 1] == nums[i] + 1:
                temp_sub += 1
                max_sub = max(max_sub, temp_sub)
            else:
                temp_sub = 1
        return max_sub

    #  其实在要求时间复杂度的前提下，直接定义好集合就可以了，确实没有必要对数组进行排序了
    def longestConsecutive2(self, nums):
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res

    # 法三，用字典或者hash记录目前与该值可以组成的最长连续序列
    def longestConsecutive3(self, nums):
        # 记录首尾值的最长长度
        lookup = defaultdict(lambda: 0)
        res = 0
        for num in nums:
            left, right = lookup[num - 1], lookup[num + 1]
            # 记录长度
            lookup[num] = lookup[num - left] = lookup[num + right] = left + right + 1
            res = max(res, left + right + 1)
        return res


if __name__ == '__main__':
    nums = [1,2,0,1]
    s = Solution()
    print(s.longestConsecutive3(nums))