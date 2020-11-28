# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if not t2: return t1
        def dfs(t1, t2):
            if not t1 or not t2:
                return t1 if t1 else t2
            t1.val += t2.val
            t1.left = dfs(t1.left, t2.left)
            t1.right = dfs(t1.right, t2.right)
            return t1
        return dfs(t1, t2)

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if not t2: return t1
        stack = [(t1, t2)]
        while stack:
            c1, c2 = stack.pop(0)
            c1.val += c2.val
            if c1.left and c2.left:
                stack.append((c1.left, c2.left))
            elif c2.left:
                c1.left = c2.left

            if c1.right and c2.right:
                stack.append((c1.right, c2.right))
            elif c2.right:
                c1.right = c2.right
        return t1
