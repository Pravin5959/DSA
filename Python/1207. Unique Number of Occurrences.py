'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Explanation : This problem requires understanding of set and hash map data structure

Step1 : As we need to map first the occurances of each elements in the list input, we will have to use hash map, in python we can use a Counter function with iterable argument to create a dictionary with elements count
Step2 : Once we have the dictionary, we can use a set to have a look up table for the values being inserted from the dict values
Step3 : If any of them, are already looked up present then we will return false else we will return true

Time complexity:
O(n), we are creating counter and iterating the counter the max complexity is n+n = 2n

Space complexity:
O(n), as we are using dict and set, so overall n+n = 2n
'''
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        checker, counter = set(), Counter(arr)
        for value in counter.values():
            if value in checker: return False
            checker.add(value)
        return True
