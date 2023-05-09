# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0  # initialize start pointer to the first index
        end = len(nums)-1  # initialize end pointer to the last index
        while start <= end:  # loop until start is greater than end
            mid = (start + end)//2  # calculate the middle index
            if nums[mid] == target:  # if target is found at mid index
                return mid
            elif nums[mid] > target:  # if target is smaller than the mid value
                end = mid - 1  # update end to mid - 1 for searching the left half
            else:  # if target is greater than the mid value
                start = mid + 1  # update start to mid + 1 for searching the right half
        return end+1  # if target is not found, return the index where it should be inserted

# time complexity is O(log n) 