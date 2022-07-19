# Question: https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Solution for Leetcode

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coor = coordinates

        # differece between ordinates of first two consecutive coordinates.
        Y = (coor[1][1] - coor[0][1])

        # differece between abscissa of first two consecutive coordinates.
        X = (coor[1][0] - coor[0][0])

        # Slope of first two consecutive coordinates
        # Slope == 100 if line is vertical.
        m = Y/X if X else 100
        # print(m)

        # Looping over all the coordinates and calculating
        # slopes among consecutive coordinates.
        for i in range(len(coor)-1):
            Y = (coor[i+1][1] - coor[i][1])
            X = (coor[i+1][0] - coor[i][0])
            M = Y/X if X else 100
            # print(M)

            # if slope is not equal to the slope of first two consecutive coordinates.
            # return False
            if M != m:
                return False
        
        # if all the slopes are equal to m, return True.
        return True