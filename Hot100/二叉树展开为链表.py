# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 最直白的解决方法
class Solution:
    # 一看示例可知，是按照前序遍历的方式进行展开
    def pre_order(self, root: TreeNode) -> []:
        res = []
        if root is None:
            return res
        res.append(root.val)
        res += self.pre_order(root.left)
        res += self.pre_order(root.right)
        return res

    def flatten(self, root: TreeNode):
        pre_order = self.pre_order(root)
        n = len(pre_order)
        count = 0
        cur = root
        while cur and count < n:
            cur.val = pre_order[count]
            count += 1
            cur.left = None
            if count < n:
                cur.right = TreeNode(pre_order[count])
            else:
                cur.right = None
            cur = cur.right


# 该如何考虑新的解决办法？
# 递归对左子树和右子树进行后序遍历后，将右子树赋给左子树的最右节点。将左子树赋给右子树，将左子树置空。再每层递归去处理这个问题。
class Solution2:
    def flatten(self, root: TreeNode):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None


if __name__ == '__main__':
    s = Solution2()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n5.right = n6
    s.flatten(n1)