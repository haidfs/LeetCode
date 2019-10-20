# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# 解题时要非常注意一点，题目不会平白无故的出出来，对于大多数题目而言，都是存在要考查的那个点。
# 想不到考点的时候可以看一下题目带的标签，对标签没有想法的可以直接看题解了
# 这道题考查的是递归回溯加剪枝算法
# 思路：以 target = 7 为根结点，每一个分支做减法。减到 00 或者负数的时候，剪枝。其中，减到 00 的时候结算，这里 “结算” 的意思是添加到结果集。
# 在回溯情况下如何去重？即如何剪枝
# 利用减法把递归的树图画出来，出现重复的原因是因为后面分支的更深层的边出现了前面分支低层的边的值。，所以需要对candidate这个数组进行排序
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        # 递归终止、递归拆分、递归转化为动态规划
        if target == 0:
            res.append(path[:])
            return
        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                return
                # break
            path.append(candidates[index])
            self.__dfs(candidates, index, size, path, res, residue)
            # 每一层走完之后，有就append，没有因为进行了排序，当走到loop里面的时候，发现residue会小于-1，所以会直接break回到上一层
            path.pop()

    # 考虑使用标准的递归模板
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [2, 3, 6, 7]
    target = 7
    print(s.combinationSum2(arr, target))