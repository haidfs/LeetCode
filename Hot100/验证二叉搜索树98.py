# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 这样的写法是有问题的，因为不光是要根节点和左右子节点进行比较，而是需要根节点与左右子树进行比较
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left:
            if root.val < root.left.val:
                return False
        if root.right:
            if root.val > root.right.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.midTraverse(root)
        if len(inorder) <= 1:
            return True
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True

    def midTraverse(self, root: TreeNode):
        res = []
        if not root:
            return res
        res += self.midTraverse(root.left)
        res.append(root.val)
        res += self.midTraverse(root.right)
        return res


class Solution3:
    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not self.helper(node.right, val, upper):
            return False
        if not self.helper(node.left, lower, val):
            return False
        return True


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l2.left = l1
    l2.right = l3
    s = Solution3()
    print(s.isValidBST(l2))