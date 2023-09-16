'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Explanation: This problem requires understanding of two pointers
Step1 : We need to assign two pointers i, j to 0 and then move the jth index if the value over it is 0 else we will swap the value at i and j and increament them
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0: j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j+1
