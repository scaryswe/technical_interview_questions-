# question

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


#My notes
# brute force solution: Double for loop O(n^2)

# the best solution would be to create a hashmap to store each indecies data so it wouldn't have to 
# be iterated over again O(n)

#pseudocode create a hashmap that stores value : index. Do not initialize hashmap to ensure each value 
# is only iterated through once since we cant use the same index twice to reach our target. Do target - index
# to find the value of the of the only number that could be used to sum to target then check the array for it. 
#repeat.




# solution

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         d = {}
#         for i, j in enumerate(nums):
#             r = target - j
#             if r in d: return [d[r], i]
#             d[j] = i

#mysolution

 class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_dict = {}
        for i in range(len(nums)):
           diff = target - range 
           if diff in diff_dict: return [diff_dict[r], i]
           d[range] = i
           


# Time complexity is O(n)