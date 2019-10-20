class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        left, right = -1, -1
        if target == nums[0]:
            left = 0
        if target == nums[-1]:
            right = len(nums) - 1
        if left == -1:
            left = self.searchLeft(nums, target, 0, len(nums) - 1)
        if right == -1:
            right = self.searchRight(nums, target, 0, len(nums) - 1)
        return [left, right]

    def searchLeft(self, nums: [int], target: int, left, right) -> [int]:
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] < target and nums[pivot + 1] == target:
                return pivot + 1
            elif nums[pivot] < target and nums[pivot + 1] < target:
                left = pivot + 1
            elif nums[pivot] == target or nums[pivot] > target:
                right = pivot - 1
            else:
                return -1
        return -1

    def searchRight(self, nums: [int], target: int, left, right) -> [int]:
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target and nums[pivot + 1] > target:
                return pivot
            elif nums[pivot + 1] < target or nums[pivot + 1] == target:
                left = pivot + 1
            elif nums[pivot] > target and nums[pivot + 1] > target:
                right = pivot - 1
            else:
                return -1
        return -1


# 第一种方法，严格来说是不适合的，因为使用了两个3*3的棋盘来判断对应的递归条件
# 棋盘大的原因是因为一个有大于等于小于三种情况，需要尽可能的减小棋盘
# 因为时间复杂度的原因。需要对原本的二分查找算法进行修改，和之前的旋转数组一样，也是两次二分法来操作。
# 两次二分法来确定左右边界，在找到一个target之后不会立即停止，需要继续搜索，直到lo==hi且他们在某个target值处下标相同
#

class Solution2(object):
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


if __name__ == '__main__':
    s = Solution2()
    nums = [1, 8, 8, 8, 8, 8, 8, 8, 8, 1]
    # nums = [1]
    target = 8
    print(s.searchRange(nums, target))