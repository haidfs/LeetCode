# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        num1_str, num2_str = "", ""
        while cur1:
            num1_str += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            num2_str += str(cur2.val)
            cur2 = cur2.next
        test = int(num1_str[::-1]) + int(num2_str[::-1])
        print(test)
        sum_str = str(int(num1_str[::-1]) + int(num2_str[::-1]))[::-1]
        length = len(sum_str)
        if length == 1:
            return ListNode(int(sum_str[0]))

        cur = ListNode(int(sum_str[0]))
        second = ListNode(int(sum_str[1]))
        cur.next = second

        new_head = cur
        cur = cur.next
        for i in range(2, length):
            cur.next = ListNode(int(sum_str[i]))
            cur = cur.next
        return new_head


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(8)
    l3 = ListNode(6)
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(8)
    l7 = ListNode(3)
    l8 = ListNode(5)
    l9 = ListNode(7)
    l10 = ListNode(6)
    l11 = ListNode(7)
    l12 = ListNode(8)
    l13 = ListNode(0)
    l14 = ListNode(8)
    l15 = ListNode(5)
    l16 = ListNode(8)
    l17 = ListNode(9)
    l18 = ListNode(7)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    l7.next = l8
    l8.next = l9
    l10.next = l11
    l11.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15
    l15.next = l16
    l16.next = l17
    l17.next = l18
    s = Solution()
    s.addTwoNumbers(l1, l10)