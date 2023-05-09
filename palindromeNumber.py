# Question
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

# **********************************************************************************

# Solution for follow up
def isPalindrome(x):
    # If x is negative or ends in a zero (except 0 itself), it cannot be a palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # Initialize a variable to store the reversed integer
    reversed_num = 0
    
    # While x is greater than the reversed integer, keep dividing x by 10 and adding the remainder to the reversed integer
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    # If the length of x is odd, we can ignore the middle digit
    # by dividing reversed_num by 10
    return x == reversed_num or x == reversed_num // 10



