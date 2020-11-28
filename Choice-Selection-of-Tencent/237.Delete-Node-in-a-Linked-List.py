# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 如何让自己在世界上消失，但又不死？ —— 将自己完全变成另一个人，再杀了那个人就行了。
        # One-line Solution
        # node.val, node.next = node.next.val, node.next.next
        node.val = node.next.val
        node.next = node.next.next
