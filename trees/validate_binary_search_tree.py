# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev_val = None
        # Start the recursive in order traversal
        return self._validate_inorder(root)
    
    def _validate_inorder(self, node):
        
        # Base case is empty subtree, which is always valid
        if node is None:
            return True
        
        # Check left subtree recursively
        if not self._validate_inorder(node.left):
            return False
        
        # Main comparison of root with nodes
        if self.prev_val is not None and node.val <= self.prev_val:
            return False
        
        # Update previous value
        self.prev_val = node.val
        
        # Check rigt subtree
        return self._validate_inorder(node.right)
        
        
