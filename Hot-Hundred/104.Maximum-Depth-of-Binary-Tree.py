# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recur(cur):
            if not cur: return 0
            return max(recur(cur.left), recur(cur.right)) + 1

        return recur(root)
