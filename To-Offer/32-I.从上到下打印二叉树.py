# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop(0)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            res.append(node.val)

        return res
