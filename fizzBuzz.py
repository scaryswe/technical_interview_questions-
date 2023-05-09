# Question
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

# Constraints:

# 1 <= n <= 104

# solution

def fizzbuzz(number):
    # Loop through numbers 1 to `number`
    for i in range(1, number +1):
        # Check if number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        # Check if number is divisible by 3
        elif i % 3 == 0:
            print("fizz")
        # Check if number is divisible by 5
        elif i % 5 == 0:
            print("buzz")
        # If number is not divisible by either 3 or 5, print the number
        else:
            print(i)

# Call the function with an argument of 20
fizzbuzz(20)

# The time complexity is O(n)