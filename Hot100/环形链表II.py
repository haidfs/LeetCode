# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            h = head
            pos = 0
            while h != fast:
                h = h.next
                pos += 1
                fast = fast.next
            return "tail connects to node index %d" % pos
        except:
            return "no cycle"