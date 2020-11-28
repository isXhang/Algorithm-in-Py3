# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return

        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        n = len(stack)
        dummy = None
        for index in range(n//2):
            left, right = stack[index], stack[n-index-1]
            stack[n-index-2].next = None
            if dummy:
                dummy.next = left
            left.next = right
            dummy = right

        if n//2:
            dummy.next = stack[n//2]
            dummy.next.next = None
