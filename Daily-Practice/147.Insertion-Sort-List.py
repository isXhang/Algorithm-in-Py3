# Date: 2020-11-20
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertSort(self, values):
        for i in range(1, len(values)):
            j = i-1
            curVal = values[i]
            while j >= 0 and values[j] > curVal:
                j -= 1
            values.pop(i)
            values.insert(j+1, curVal)

    def insertionSortList(self, head: ListNode) -> ListNode:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        self.insertSort(values)
        cur = head
        for value in values:
            cur.val = value
            cur = cur.next
        return head

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        lastSort = head
        cur = head.next

        while cur:
            if lastSort.val <= cur.val:
                lastSort = cur
            else:
                prev = dummy
                while prev.next and prev.next.val <= cur.val:
                    prev = prev.next
                lastSort.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSort.next
        return dummy.next
