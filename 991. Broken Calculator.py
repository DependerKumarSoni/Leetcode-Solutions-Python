# Question: https://leetcode.com/problems/broken-calculator/

# Solution for Leetcode

# Here we will follow target to startValue approach.
# As we are allowed to either multiply startValue with 2 or subtract 1 from startValue to get Target.
# In our approach, we'll either divide target by 2 or add 1 to target to achieve startValue.
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # if startValue is greater than target, we can only perform subtraction. (as per question)
        if startValue >= target:
            return startValue-target
        # if target is divisible by 2, we will increament the number of operation and call brokenCalc again.
        if target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target//2)
        
        # if target is not divisible by 2, we can only add 1 to it.
        return 1 + self.brokenCalc(startValue, target+1)