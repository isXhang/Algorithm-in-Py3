# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.mark = None
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB: return None
#         while headA:
#             headA.mark = 1
#             headA = headA.next
#         while headB:
#             if headB.mark == 1: return headB
#             headB = headB.next
#         return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Timeout
        while headB:
            cur = headA
            while cur:
                if cur == headB: return cur
                else:
                    cur = cur.next
            headB = headB.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashmap = set()
        while headB:
            hashmap.add(headB)
            headB = headB.next
        while headA:
            if headA in hashmap: return headA
            headA = headA.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
