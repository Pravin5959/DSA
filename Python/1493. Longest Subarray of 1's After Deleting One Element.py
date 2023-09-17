'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

Explanation : This problem requires the understanding of dynamic size sliding window in algorithms
Step1 : As we need to find the max consecutive 1's in a subarry that can be created by removing one zero from it, we will initialize the 
        indexes, result storer and most importantly a count tracker of 0's in the iteration
Step2 : This counter will help us consider always only 1 0's in the window while the iteration is being computed, if the count goes 
        above 1 then we need to remove the leading zeros where our starting index of window will help
Step3 : Finally, at each instances we will compute the max size reached at each interval using the starting and ending index of the 
        window

Time complexity:
O(n), as we are traversing the input list ast most n+n = 2n times

Space complexity:
O(1), as we are using constant spaces
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j, glb_max, cnt = 0, 0, 0, 0
        while j<len(nums):
            cnt += 1 if nums[j] == 0 else 0
            while cnt > 1:
                cnt -= 1 if nums[i] == 0 else 0
                i += 1
            glb_max = max(j-i, glb_max)
            j += 1
        return glb_max
