# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def recur(left, right):
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return recur(left.left, right.right) and recur(left.right, right.left)
        return recur(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        import collections
        deque = collections.deque()
        deque.append((root, root))

        while deque:
            left, right = deque.popleft()
            if not left and not right: continue
            if not left or not right or left.val != right.val: return False
            deque.append((left.left, right.right))
            deque.append((left.right, right.left))
        return True
