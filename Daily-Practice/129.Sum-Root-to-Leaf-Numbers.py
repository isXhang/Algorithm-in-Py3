# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        roads = list()

        def recur(cur, road):
            if not cur: return None
            road += str(cur.val)
            if not cur.left and not cur.right:
                roads.append(road)
                return
            recur(cur.left, road)
            recur(cur.right, road)
            return road

        recur(root, "")
        return sum([int(road) for road in roads])
