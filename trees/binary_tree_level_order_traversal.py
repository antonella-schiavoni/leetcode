# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # Empty tree returns empty list
        if root is None:
            return []

        # Init the queue. This will be FIFO structure
        queue = deque([root])

        # Final list of results
        results = []

        while queue:

            # Capture the size of the current queue
            level_size = len(queue)

            # Init the list for current legel's values
            current_level = []

            # Process the nodes
            for _ in range(level_size):

                # Retrieve the node from the front
                node = queue.popleft()

                # Add the node's value to the current level list
                current_level.append(node.val)

                # Enqueue the children (left to right order)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(current_level)

        return results
        
        
