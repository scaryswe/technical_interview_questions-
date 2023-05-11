#Question

# Given two arrays a and b of numbers and a target value t, find a number 
# from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

#Solution

def find_closest_pair(a, b, t):
    # Step 1: Initialize variables to track the minimum difference found so far and the pair of numbers with that minimum difference
    min_diff = None
    closest_pair = None

    # Step 2: Iterate over each number in array a
    for num_a in a:

        # Step 3: For each number in array a, iterate over each number in array b
        for num_b in b:

            # Step 4: Calculate the sum of the current pair of numbers and the absolute difference between the sum and the target value t
            pair_sum = num_a + num_b
            diff = abs(pair_sum - t)

            # Step 5: If the absolute difference is less than the current minimum difference (or if there is no current minimum difference), update the min_diff and closest_pair variables
            if min_diff is None or diff < min_diff:
                min_diff = diff
                closest_pair = [num_a, num_b]

    # Step 6: Return the closest_pair variable
    return closest_pair
