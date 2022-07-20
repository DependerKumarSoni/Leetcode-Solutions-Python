# Question: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Solution for Leetcode:

class Solution:
    def minDepth(self, root) -> int:
        
        # Base Case
        if not root:
            return 0
        
        # Call to left sub tree
        left = self.minDepth(root.left) 

        # Call to right sub tree
        right = self.minDepth(root.right)

        
        if left == 0:
            return right + 1
        
        if right == 0:
            return left + 1
        
        # returning minimum of left and right (+1 to avoid 0 indexing of depth)
        return min(left, right) + 1