# Question: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Solution for Leetcode:

# In this question, we are starting from lower left corner of matrix.
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix) # no. of rows
        n=len(matrix[0]) # no. of columns
        
        i=m-1 # last index of rows.
        j=0 # starting index of columns.
        
        while i>=0 and j<n:
            
            # if target meets, return True.
            if matrix[i][j]==target:
                return True
            
            # if current value becomes lesser than target, increment column.
            elif matrix[i][j]<target:
                j+=1

            # else keep decreasing row.
            else:
                i-=1
        
        # if value not found, return False.
        return False