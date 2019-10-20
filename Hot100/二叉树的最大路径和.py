# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#
#        1
#       / \
#      2   3
#
# 输出: 6
# 示例 2:
#
# 输入: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# 输出: 42
# 首先需要考虑一个简化的函数，参数是一个顶点，计算它及其子树的最大贡献
# 换句话说，就是计算包含这个顶点的最大权值路径，但是当一棵树的根节点为负值时，最大路径不一定包含根节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) :
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum