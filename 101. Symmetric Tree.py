# Question: https://leetcode.com/problems/symmetric-tree/

# Solution for Leetcode

class Solution:
    # This is the helper function to compare child node and child of child node.
    def compare(self,rootleft,rootright):
        if rootleft == None or rootright == None:
            return rootleft==rootright
        return rootleft.val == rootright.val and self.compare(rootleft.left,rootright.right) and self.compare(rootleft.right,rootright.left)
    
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)