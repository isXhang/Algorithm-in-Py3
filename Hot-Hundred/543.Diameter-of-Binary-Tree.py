# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        return 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            res.append(self.maxDepth(node.right) + self.maxDepth(node.left))
        return max(res)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        def depth(cur):
            self.ans
            if not cur: return 0
            L = depth(cur.left)
            R = depth(cur.right)
            self.ans = max(self.ans, L+R)
            return max(L, R) + 1
        depth(root)
        return self.ans
