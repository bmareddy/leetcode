# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
sum of values beteen L and R
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = []
        def traverse_node(node, L, R, result):
            if node:
                if node.val >= L and node.val <= R:
                    result.append(node.val)
                if node.val < L:
                    node.left = None
                if node.val > R:
                    node.right = None
                traverse_node(node.right, L, R, result)
                traverse_node(node.left, L, R, result)
        traverse_node(root, L, R, result)
        return sum(result)