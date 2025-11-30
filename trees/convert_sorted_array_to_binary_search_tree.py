# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self._convert(nums, 0, len(nums) - 1)
        
    def _convert(self, nums, start, end):

        # Base case, when the range is empty
        if start > end:
            return None

        # Find the middle element
        mid_point = (start + end) // 2

        # Create a tree node with the middle element
        root = TreeNode(nums[mid_point])

        # Recursive calls

        # Build the left subtree using the array section BEFORE the midpoint
        root.left = self._convert(nums, start, (mid_point-1))

        # Build the right subtree using the array section AFTER the midpoint
        root.right = self._convert(nums, mid_point + 1, end)

        # Return the node (which is already connected)
        return root
        
