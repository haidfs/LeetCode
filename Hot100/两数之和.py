# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    # 首先要做的事还是看清楚题目，不然会被边界测试阻挡很多次
    def twoSum(self, nums: [int], target: int) -> [int]:
        res = []
        length = len(nums)
        if not nums:
            return res
            # 根据数值大小将索引进行排序
        sort_index = sorted(range(length), key=lambda k: nums[k])
        sort_nums = sorted(nums)
        visit_flag = [False for _ in range(length)]
        for i in range(length):
            res = []
            if not visit_flag[i]:
                num1 = sort_nums[i]
                res.append(sort_index[i])
                visit_flag[i] = True
                for j in range(i + 1, length):
                    if sort_nums[j] == target - num1 and not visit_flag[j]:
                        res.append(sort_index[j])
                        visit_flag[j] = True
                        if len(res) == 2:
                            return sorted(res)
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(s.twoSum(nums, target))