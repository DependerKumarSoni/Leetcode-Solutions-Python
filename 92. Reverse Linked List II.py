# Question: https://leetcode.com/problems/reverse-linked-list-ii/

# Solution for Leetcode:

# This solution is using extra space for storing values and nodes.
# Later I'll try to do the same without extra space.

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        # to stores the values that needed to be reverse.
        values = []
        # to keep track of the nodes which needs to be reverse.
        nodes = []

        counter = 0
        curr = head
        while curr:
            counter += 1
            if counter >= left and counter <= right:
                # Storing Values and Nodes between Left and Right.
                values.append(curr.val)
                nodes.append(curr)
            curr = curr.next
        
        # Overwriting values of nodes from stored values and nodes.
        for node in nodes:
            node.val = values.pop(-1)

        # Returning the head.
        return head