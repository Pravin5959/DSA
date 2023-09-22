'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/

Explanation : This problem requires understanding of prefix and suffix sum pattern in algorthim
Step1 : As we need to find the pivot index, before which and after which the sum of the elements will be equal, we will consider calculating the initial states of the sums by 0 and total sum of the elements in the list
Step 2 : As we need to find the leftmost pivot index, so we will start subtracting and elements from left and check the total sum from left with the subtracted sum, the point it is equal will be the pivot index

Illustration :
For any index i in a list of length n the pivot index should satisty the below condition

sum(0 to n) - sum(0 to i) = sum(0 to i-1)
# right sum = left sum

If none of them satisfies, then -1 needs to be returned

Time complexity:
O(n), as we are travering the list at max n+n = 2n times

Space complexity:
O(1), as we are using constant space across program
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        start, end = 0, sum(nums)
        for idx, ele in enumerate(nums):
            end -= ele
            if start == end: return idx
            start += ele
        return -1
