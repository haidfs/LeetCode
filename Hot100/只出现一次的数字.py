# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            elif i == len(nums) - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]
            else:
                if nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                    return nums[i]
        return 0