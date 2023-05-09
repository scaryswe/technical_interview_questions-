# Question
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack
        stack = []
        # Loop through each character in the string
        for char in s:
            # If the character is an opening bracket, add it to the stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            # If the character is a closing bracket, check if it matches the top of the stack
            else:
                # If the stack is empty, the string is invalid
                if not stack:
                    return False
                # If the closing bracket matches the top of the stack, pop it off
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                # If the closing bracket doesn't match the top of the stack, the string is invalid
                else:
                    return False
        # If there are no more characters in the string and the stack is empty, the string is valid
        return not stack

