# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def _is_mirror(self, node_1, node_2):
        # 3 Base conditions
        
        # 1. Both nodes are null, so they are symetrical
        if node_1 is None and node_2 is None:
            return True 
        
        # 2. We are not under symetrical conditions
        if (node_1 is None and node_2 is not None) or (node_1 is not None and node_2 is None):
            return False

        # 3. Values of the nodes don't match
        if  node_1.val != node_2.val:
            return False

        return self._is_mirror(node_1.left, node_2.right) and self._is_mirror(node_1.right, node_2.left)
    
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        # An empty tree is symetric
        if root is None:
            return True
        
        # Recursion: compare left and right node
        return self._is_mirror(root.left, root.right)
        
