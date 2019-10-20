from functools import reduce


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = []
        for i in range(len(nums)):
            res.append(reduce(lambda x, y: x * y, nums[:i] + nums[i + 1:]))
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 4]
    print(s.productExceptSelf(arr))