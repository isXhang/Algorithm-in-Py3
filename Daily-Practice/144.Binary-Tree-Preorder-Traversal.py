# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recur(cur):
            if not cur: return
            res.append(cur.val)
            recur(cur.left)
            recur(cur.right)
        recur(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

# Morris Traversal: non-recursive, no stacks, O(n) in Time and O(1) in Space
