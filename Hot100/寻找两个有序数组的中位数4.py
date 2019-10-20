# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0
# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5

# 第一种直接合并两个有序列表，时间复杂度为O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0:
            mid = self.getMid(nums2)
            return mid
        if len2 == 0:
            mid = self.getMid(nums1)
            return mid
        merge = []
        while nums2 and nums1:
            if nums1[0] < nums2[0]:
                merge.append(nums1.pop(0))
            else:
                merge.append(nums2.pop(0))
        if nums1:
            merge.extend(nums1)
        if nums2:
            merge.extend(nums2)
        mid = self.getMid(merge)
        return mid

    def getMid(self, nums):
        length = len(nums)
        if length % 2 == 0:
            mid = (nums[length // 2] + nums[length // 2 - 1]) / 2
        else:
            mid = float(nums[length // 2])
        return mid

class Solution2:
    # 题目要求时间复杂度为O(log(m+n))，这里很明显就是二分算法，但是二分算法如何使用，还需要仔细分析
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        pass
if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3]
    print(s.findMedianSortedArrays(nums1, nums2))