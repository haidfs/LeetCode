class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return []
        current_layer = [root]
        res = [[root.val]]
        while current_layer:
            next_layer = []
            res_part = []
            for i in current_layer:
                if i.left:
                    next_layer.append(i.left)
                    res_part.append(i.left.val)
                if i.right:
                    next_layer.append(i.right)
                    res_part.append(i.right.val)
            current_layer = next_layer
            if res_part:
                res.append(res_part)
        return res


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