# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
	# Space Complexity O(n)

        # current = head
        # res = []
        # while current:
        #     res.append(current.val)
        #     current = current.next
        # return res == res[::-1]

        if not head: return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        while pre:
            if pre.val != head.val:
                return False
            pre, head = pre.next, head.next
        return True
