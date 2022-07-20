# Question:

# Solution for Leetcode:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def paths(r,target,sums):
            if r is not None:
			#temp value for storing current sum
                temp = sums + r.val
				#check if current node has no children and if the target matches the current sum, return true
                if r.left is None and r.right is None:
                    if target == temp:
                        return True
                    else:
                        return False
                else:
				#if current node has children, recursively check for left and right children, 
				#since function returns boolean, if either one of the two recursive calls is true, then return true
                    if paths(r.left,target,temp) or paths(r.right,target,temp):
                        return True
                    else:
                        return False
		#inititalize current sum to 0 when calling
        return paths(root,targetSum,0)