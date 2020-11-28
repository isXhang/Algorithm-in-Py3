# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        if length == 0:
            return None
        if length == 1:
            return lists[0]

        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = head = ListNode(0)
        while heap:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        return head.next
