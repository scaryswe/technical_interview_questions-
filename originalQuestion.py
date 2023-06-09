# Write a function that takes a list of integers as input and returns the sum of all the even integers in the list.

# Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = sum_even_numbers(numbers)
# print(result)  # Output: 20


#Solution
def sum_even_numbers(numbers):
    # Initialize a variable to store the total sum
    total = 0
    # Loop through each number in the list
    for i in range(numbers):
        # Check if the number is even (i.e., divisible by 2 with no remainder)
        if i % 2 == 0:
            # If the number is even, add it to the total sum
            total += i
    # Return the total sum of even numbers
    print(total)

#  time complexity is O(n)

sum_even_numbers(10)


# two questions, why did i get type error when I didnt use range and why do I need to 
# say print total when i had return total