'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

Explanation : This problem requires understanding of prefix sum in algorithm
Step1 : As you know the starting point of an altitude is 0 and post that based upon the array index the altitude will increase or decrease, so we need to calculate the highest altitude a biker would have gained
Step2 : We will have to sum up the data in the list for every index until the last and check at which point in list the biker have gained the max altitude

Time complexity:
O(n), as we are traversing the list only once
Space complexity:
O(1), as we are using constant space
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum, max_val = 0, 0
        for ele in gain:
            prefix_sum += ele
            max_val = max(max_val, prefix_sum)
        return max_val
