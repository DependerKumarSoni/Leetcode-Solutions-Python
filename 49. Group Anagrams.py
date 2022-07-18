# Question: https://leetcode.com/problems/group-anagrams/

# Solution for Leetcode.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defining an empty dictionary
        Map = {} 

        # looping over the input list of strings.
        for s in strs:

            # creating a key for dictionary which is the sorted form of the string s.
            key = "".join(sorted(s)) 

            # if the key (sorted form of string) is present in Map:
            if key in Map:

                # just add this string as well into the same array
                Map[key].append(s) 
            
            # otherwise
            else: 
                
                # create a new key: value pair into the Map, where key is the sorted form of value (string s)
                Map[key] = [s] 
        
        # finally, return the list of values created inside the Map.
        return list(Map.values()) 