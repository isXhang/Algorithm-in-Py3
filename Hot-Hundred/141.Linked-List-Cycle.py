# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next: return False

        slow, fast = head, head.next
        while slow.val != fast.val:
            if not fast.next or not fast.next.next: return False
            slow, fast = slow.next, fast.next.next
        return True

    def hasCycle(self, head):
        cur = head
        while cur:
            if cur.val == '/': return True
            cur.val = '/'
            cur = cur.next
        return False
