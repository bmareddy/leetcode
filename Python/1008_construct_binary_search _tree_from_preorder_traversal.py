# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        node = TreeNode(preorder[0])
        
        def addNextNode(node: TreeNode, element: int):
            if element < node.val:
                if node.right is not None:
                    addNextNode(node.right, element)
                elif node.left is None:
                    node.left = TreeNode(element)
                else:
                    addNextNode(node.left, element)
            else:
                if node.right is None:
                    node.right = TreeNode(element)
                else:
                    addNextNode(node.right, element)
        
        for element in preorder[1:]:        
            addNextNode(node,element)
        return node