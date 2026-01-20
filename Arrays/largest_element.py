
"""
Problem: Largest Element in an Array

Given an array of integers nums, return the value of the largest element.

Example:
Input: nums = [3, 3, 6, 1]
Output: 6

Approach:
- Initialize max_val with the first element
- Traverse the array and update max_val if a larger element is found

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def largestElement(self, nums):
        max_val = nums[0]

        for num in nums:
            if num > max_val:
                max_val = num

        return max_val
