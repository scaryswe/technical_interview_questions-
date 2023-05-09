# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Solution
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        # Initialize an empty string to store the common prefix
        ans=""
        # Sort the list of strings in alphabetical order
        v=sorted(v)
        # Get the first and last string in the sorted list
        first=v[0]
        last=v[-1]
        # Loop through the characters in the shorter string (either first or last)
        for i in range(min(len(first),len(last))):
            # If the characters at the same index in first and last are not equal, return the common prefix found so far
            if(first[i]!=last[i]):
                return ans
            # Otherwise, add the character to the common prefix
            ans+=first[i]
        # Return the common prefix found
        return ans
    
    # time complexity (number) is O(n * m) 