# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, root1: TreeNode, root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right,
                                                                                                   root2.left)


if __name__ == '__main__':
    l1_1 = TreeNode(1)
    l2_1 = TreeNode(2)
    l2_2 = TreeNode(2)
    l3_1 = TreeNode(3)
    l3_2 = TreeNode(4)
    l3_3 = TreeNode(4)
    l3_4 = TreeNode(3)
    l1_1.left = l2_1
    l1_1.right = l2_2
    l2_1.left = l3_1
    l2_1.right = l3_2
    l2_2.left = l3_3
    l2_2.right = l3_4
    s = Solution()
    print(s.isSymmetric(l1_1))