'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

Explanation : This problem requires understanding of sets and hash map in data structures

Step1 : As mentioned, in the problem we have to find the distinct non presence value for each of the list with another list, so for checking the distinct value we are using set
Step2 : For knowing the presense, we are storing the distinct value as key with value being 1 for first list and 2 for second list
Step3 : Lastly, we will filter the keys from the dictionary which have 1 value for the non presence values in second list and vise versa

Time complexity:
O(n), as we are traversing the lists and dict at max n+n+n = 3n times

Space complexity:
O(n), as we are using 2 sets and 1 dict n+n+n = 3n times
'''
from collections import defaultdict
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
      op = [[],[]]
      num_dict = defaultdict(int)
      for i in set(nums1): num_dict[i] += 1
      for j in set(nums2): num_dict[j] += 2
      for key, value in num_dict.items():
        if value == 1: op[0].append(key)
        elif value == 2: op[1].append(key)
      return op
