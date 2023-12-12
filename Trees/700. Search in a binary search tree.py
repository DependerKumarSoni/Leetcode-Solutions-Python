# Question: https://leetcode.com/problems/search-in-a-binary-search-tree/

# Solution for Leetcode:

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if val < root.val:
            return self.searchBST(root.left, val)
        
        if val > root.val:
            return self.searchBST(root.right, val)
        
        return root


# Explaination:
"""
    first check if root is valid (line: 7)
    As the tree is BST (sorted), we can compare if target value is less than or greater that the current value.
    And proceed accordingly.
    
"""
