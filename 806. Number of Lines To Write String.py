# Question: https://leetcode.com/problems/number-of-lines-to-write-string/

# Solution for Leetcode

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:

        # Length is storing the sum of width of characters (c) untill it reaches 100.
        Length = 0

        # Lines is keeping the count of lines required.
        lines = 1

        # Looping over the string (s => string; c => character)
        for c in s:

            # Adding the width of character 'c' untill it reaches 100.
            Length += widths[abs(ord(c) - ord("a"))]

            # if length becomes greater than 100
            if Length > 100:

                # Updating Length to the last character due to which length became > 100.
                Length = widths[abs(ord(c) - ord("a"))]

                # Incrementing the number of lines
                lines += 1
        
        # returning the required answer.
        return [lines, Length]