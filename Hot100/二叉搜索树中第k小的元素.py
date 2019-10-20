class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        order = self.midTraverse(root)
        return order[k - 1]

    def midTraverse(self, root):
        res = []
        if not root:
            return res
        res.append(root.val)
        res += self.midTraverse(root.left)
        res += self.midTraverse(root.right)
        return res


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n3.left = n1
    n3.right = n4
    n1.right = n2
    print(s.kthSmallest(n3, 1))