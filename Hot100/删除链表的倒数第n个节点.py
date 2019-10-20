class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 这个问题考虑到一些情况，需要使用dummy节点
        # 比如说仅仅只具有一个节点，需要删除倒数第一个节点的case
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    s = Solution()
    s.removeNthFromEnd(l1, 2)
