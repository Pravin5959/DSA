'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

Explanation: This question requires undertanding of comparitions while iterations
Step1 : As we need a increasing subsequence of three numbers from the array, we know that num1 > num2 > num3, but the array can 
        have numbers randomly available
Step2 : num1 will store the least number, means whenever a number lesser than num1 comes, we will update it, similarly for num2,
        but if nothing is getting updated anymore means we got the increasing sequence

Time Complexity : O(n), as we are iterating the list once
Space Complexity : O(1), as we are using constant space
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
        return False
