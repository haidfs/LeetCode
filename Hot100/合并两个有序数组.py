from copy import deepcopy


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cp = deepcopy(nums1[:m])
        if cp is None:
            nums1 = nums2
            return nums1
        if nums2 is None:
            return
        for _ in range(len(nums1)):
            nums1.pop()
        nums2 = nums2[:n]
        while cp and nums2:
            if cp[0] < nums2[0]:
                nums1.append(cp.pop(0))
            else:
                nums1.append(nums2.pop(0))
        if cp:
            nums1.extend(cp)
        if nums2:
            nums1.extend(nums2)
        return nums1


if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s = Solution()
    print(s.merge(nums1, m, nums2, n))