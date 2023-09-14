'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Explanation: This is medium based problem which can be optimally solved inplace
Step1 : As we know there are two possibilities, one is input without any 0, with 1 zero and with more than 1 zeros
Step2 : There is no issue in first scenario without zero, as we just have to divide each elements with the overall multiplied value
Step3 : With single zero, we just need to put the overall multiplied value at the place of zero
Step4 : With multiple zeros, its pretty clear that the whole list itself will be zero

Time Complexity: O(n), we are traversing the list twice n + n, so overall complexity becomes O(n)
Space Complexity : O(1), we are not using any extra space in the whole execution because of inplace replacement
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      mul_val, zero_cnts = 1, 0
      for val in nums:
        if val == 0: zero_cnts += 1
        else: mul_val = mul_val*val
      for idx, val in enumerate(nums):
        if zero_cnts > 1: nums[idx] = 0
        else: nums[idx] = mul_val if zero_cnts == 1 and val == 0 else int(mul_val/nums[idx]) if zero_cnts == 0 else 0
      return nums
