#Question

# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

#Solution

def find_largest_values(a, k):
    # Step 1: Sort the array in descending order
    a.sort(reverse=True)

    # Step 2: Take the first k values of the sorted array
    largest_values = a[:k]

    # Step 3: Return the largest_values list
    return largest_values
