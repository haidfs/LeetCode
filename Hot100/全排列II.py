# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        def backtrack(nums,tmp):
            nonlocal res
            if not nums and tmp not in res:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])

        res=[]
        backtrack(nums,[])
        return res