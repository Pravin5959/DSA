'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

Explanation : This problem requires the understanding of dynamic size sliding window in algorithms
Step1 : As we need to find the max consecutive 1's in a subarry that can be created by flipping at most k 0's to 1, we will 
        initialize the indexes, result storer and most importantly a count tracker of 0's in the iteration
Step2 : This counter will help us consider always at most k zeros in the window while the iteration is being computed, if the 
        count goes above k then we need to remove the leading zeros where our starting index of window will help
Step3 : Finally, at each instances we will compute the max size reached at each interval using the starting and ending index of 
        the window

Time complexity:
O(n), as we are traversing the input list ast most n+n = 2n times

Space complexity:
O(1), as we are using constant spaces
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j, cnt, glb_max = 0, 0, 0, 0
        while j<len(nums):
            cnt += 1 if nums[j] == 0 else 0
            while cnt > k:
                cnt -= 1 if nums[i] == 0 else 0
                i += 1
            glb_max = max(j-i+1, glb_max)
            j += 1
        return glb_max
