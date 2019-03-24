# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        get max and position
        assign max value to node value, return node
        recursively call the function to assign left and right based on array split
        break when no elements remain
        """
        if nums == []:
            return None
        
        max_val = max(nums)
        max_pos = nums.index(max_val)
        node = TreeNode(max_val)
        node.left = self.constructMaximumBinaryTree(nums[:max_pos])
        node.right = self.constructMaximumBinaryTree(nums[max_pos+1:])
        
        return node