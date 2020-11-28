# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def recur(cur):
            nonlocal total
            if cur:
                recur(cur.right)
                total += cur.val
                cur.val = total
                recur(cur.left)

        if not root: return None
        total = 0
        recur(root)
        return root
