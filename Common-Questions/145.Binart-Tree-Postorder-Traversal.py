# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recur(cur):
            if not cur: return
            recur(cur.left)
            recur(cur.right)
            res.append(cur.val)
        recur(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        node = root
        prev = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or prev == node.right:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return res
