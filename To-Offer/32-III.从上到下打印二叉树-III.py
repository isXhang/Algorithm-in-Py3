# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = [root]
        res = []
        count = 1
        while stack:
            tmp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                tmp.append(node.val)
            if count%2: res.append(tmp)
            else: res.append(tmp[::-1])
            count += 1
        return res
