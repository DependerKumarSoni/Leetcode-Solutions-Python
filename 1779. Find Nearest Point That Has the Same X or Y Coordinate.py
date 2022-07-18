# Question: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        # setting index = -1 because if it is not modified then anser does not exist.
        index = -1

        # setting dis to be +ve infinity because we want take minimum Manhattan distance.
        dis = float("inf")

        # enumerating over the given array of coordinates.
        for i, p in enumerate(points):

            # creating another variable with infinite value to calculate distance locally.
            temp_dis = float("inf")
            
            # Case 1: If x coordinates match; then temp_dis is the mod of difference of y coordinates.
            if p[0] == x:
                temp_dis = abs(p[1]-y)
                    
            # Case 2: If y coordinates match; then temp_dis is the mod of difference of x coordinates.
            elif p[1] == y:
                temp_dis = abs(p[0]-x)

            # if temp_dis is lesser than dis, update dis and index.   
            if temp_dis < dis:
                dis = temp_dis
                index = i

        # Finally, return the required index.            
        return index