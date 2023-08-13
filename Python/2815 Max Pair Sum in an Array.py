"""
You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.

 

Example 1:

Input: nums = [51,71,17,24,42]
Output: 88
Explanation: 
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88. 
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.
 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 10^4 

Explanation:
1st : I have created a dictonary of lists which will contain key's as the max_digits present in the input list and value as the
      elements of list
      For eg: [51,71,17,24,42] the ouput dict will be { 4: [24, 42], 5:[51], 7:[71,17]}
2nd : Next I've just added first two maximum elements for the list having length greater than 1 in the dict and finally taking 
      maximum of all the values that I'll get
      For eg : [66, 88] will be the output of first part, in second part we are just finding the max([66,88]) which is 88
"""


from collections import defaultdict
import heapq
class Solution(object):
    def maxDigitSorting(self, nums):
        dig_dicts = defaultdict(list)
        for i in nums: 
            dig_dicts[int(sorted(str(i))[-1])].append(i)
        return dig_dicts 
    def maxSum(self, nums):
        max_l = [sum(heapq.nlargest(2,value)) for key, value in self.maxDigitSorting(nums).items() if len(value) > 1]
        return max(max_l) if len(max_l)>=1 else -1
