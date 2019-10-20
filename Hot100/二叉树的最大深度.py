class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        current_layer = [root]
        depth = 0
        while current_layer:
            next_layer = []
            for i in current_layer:
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            depth += 1
            current_layer = next_layer
        return depth


if __name__ == '__main__':
    s = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    print(s.maxDepth(l1))