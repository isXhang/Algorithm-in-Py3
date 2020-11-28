# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recur(cur):
            if not cur: return
            recur(cur.left)
            res.append(cur.val)
            recur(cur.right)
        recur(root)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
