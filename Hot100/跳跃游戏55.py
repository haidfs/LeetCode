# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 这道题可以想到需要用到递归回溯，甚至可以考虑到要使用动态规划，但是贪心很难想到，前二者的代码并不好写。
# 第一个方法，回溯法
# 模拟从第一个位置跳到最后位置的所有方案，从第一个位置开始，模拟所有可以跳到的位置，然后从当前位置重复上述操作，当没有办法继续跳的时候，就进行回溯。
# 递归的方法带上记忆列表之后，就成为自顶向下的动规
GOOD = 1
BAD = 0
UNKNOWN = 2


class Solution:
    def __init__(self):
        # 0代表不能跳转 1代表可以跳转，2代表未知
        self.memo = []

    def canJump(self, nums: [int]) -> bool:
        self.memo = [UNKNOWN for _ in range(len(nums))]
        self.memo[-1] = GOOD
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position, nums: [int]) -> bool:
        if self.memo[position] != UNKNOWN:
            return True if self.memo[position] == GOOD else False
        furthest_jump = min(position + nums[position], len(nums) - 1)
        for next_position in range(furthest_jump, position, -1):
            if self.canJumpFromPosition(next_position, nums):
                self.memo[position] = GOOD
                return True
        self.memo[position] = BAD
        return False


# 方法二，自底向上的动规
# 底向上和自顶向下动态规划的区别就是消除了回溯，在实际使用中，自底向下的方法有更好的时间效率因为我们不再需要栈空间，可以节省很多缓存开销。
# 更重要的事，这可以让之后更有优化的空间。回溯通常是通过反转动态规划的步骤来实现的。
class Solution2:
    def __init__(self):
        # 0代表不能跳转 1代表可以跳转，2代表未知
        self.memo = []

    def canJump(self, nums: [int]) -> bool:
        self.memo = [UNKNOWN for _ in range(len(nums))]
        self.memo[-1] = GOOD
        length = len(nums)
        for i in range(length - 2, -1, -1):
            furthest_jump = min(i + nums[i], length - 1)
            for j in range(i + 1, furthest_jump + 1):
                if self.memo[j] == GOOD:
                    self.memo[i] = GOOD
                    break
        return self.memo[0] == GOOD


# 方法三，贪心算法，在写出自底向上的模式之后，发现我们只需要找到最左边的标记为Good的坐标即可。
# 从右向左来进行查找，找到一个新的索引为good的值之后，进行新的处理，
class Solution3:
    def canJump(self, nums: [int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


if __name__ == '__main__':
    s = Solution2()
    arr = [2, 3, 1, 1, 4]
    arr2 = [3, 2, 1, 0, 4]
    print(s.canJump(arr))
