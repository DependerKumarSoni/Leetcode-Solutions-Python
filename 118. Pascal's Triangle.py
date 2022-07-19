# Question: https://leetcode.com/problems/pascals-triangle/

# Solution for Leetcode

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        # List to store rows.
        ans = []

        # Looping over Rows.
        for i in range(numRows):

            # List to store values of a row.
            temp = []

            # initial value of each row.
            val = 1

            # Looping over columns (mind the range!!!).
            for j in range(0, i+1):
                
                # Begin by entering the val to temp.
                temp.append(val)

                # this is the main part, scroll down to look at the formula.
                val = (val * (i-j))//(j+1)

            # appending the row to ans list.
            ans.append(temp)

        # returning the final answer.
        return ans

"""
Explanation:

Notice that each value of each row is following the combinations formula:
row C col

for example:
    the third column (0 indexed) of third row (0 indexed) will be:
    3 C 3 = 3! / (2! * 1!)

The first value in each row is 1. Hence set val = 1.
Now to calculate successive values, use the formula

row C col+1 = (row C col * (row - col)) // (col + 1) => Notice the '+ 1' in denominator will prevent from zero division error.
            = (val * (i - j)) // (j + 1) => This is the final formula.

"""