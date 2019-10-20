class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        res = []
        for lyst in lists:
            while lyst:
                res.append(lyst.val)
                lyst = lyst.next
        res = sorted(res)
        n = len(res)
        new_head = ListNode(0)
        cur = new_head
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return new_head.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)

    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)

    n7 = ListNode(2)
    n8 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    n7.next = n8
    s = Solution()
    lists = [n1, n4, n7]
    s.mergeKLists(lists)