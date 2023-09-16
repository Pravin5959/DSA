'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109

Explanation: This problem can be solved using two approaches using sort and two pointer which is easy to solve comparitively, 
so I'll discuss about the second approach i.e. using dictionary
Step1 : As we know, we need to count the number of times each of two elements from the list which can make a sum of k, we will 
        store a counter dictionary
Step2 : Once a counter dictionary is created we have to iterate the dictionary and check if k - key is available in the dictionary 
        or not, if it is then we will consider the min count out of both of them as min count can make the pairs with each other
Step3 : Conditions need to be written to perform calculation of one key only once and also for k - key == k, where we need to 
        consider half of the elements of same key

Time complexity: O(n), as we are iterating the list twice n+n = 2n, one for counter and one for key, value pair in counter
Space complexity: O(n), the max space complexity a dictionary will have is O(n)
'''
#first solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        storer, op = Counter(nums), 0
        for ele, cnt in storer.items():
            if ele >= k - ele and (k - ele) in storer:
                op += cnt//2 if ele == (k-ele) else min(storer[ele], storer[k-ele])
        return op
#second solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j, op = 0, len(nums)-1, 0
        nums = sorted(nums)
        while i<j:
            total_sum = nums[i]+nums[j]
            if total_sum < k: i += 1
            elif total_sum > k: j -= 1
            else: op, i, j = op+1, i+1, j-1
        return op
