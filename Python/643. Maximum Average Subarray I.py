'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
Explanation : This problem requires understanding of Sliding Window design pattern in algorithms
Step1 : As we need to check a fixed k length subarray, we need to make sure our pointers difference is k-1 elements
Step2 : To achieve that, we will use two pointers i, j where j will be moving at the end of the window anf i will be moving at 
        start of the window
Step3 : As the window will move forward after a fix length, we will make sure to remove the value which window is no more part of, 
        and wil keep of checking the max value until the complete list is iterated

Time complexity:
O(n), as we are traversing the input list at max n+n = 2n times

Space complexity:
O(1), as we are using constant space
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j, global_sum, local_sum = 0, 0, float('-inf'), 0
        while j<len(nums):
          local_sum += nums[j]
          if j-i+1 == k:
            global_sum = max(global_sum, local_sum)
            local_sum -= nums[i]
            i += 1
          j += 1
        return global_sum/k
