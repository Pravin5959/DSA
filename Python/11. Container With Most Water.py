'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Explanation : This requires understanding of two pointers
Step 1: We need two pointers i, j for start and end of the list
Step 2: As we know the water that can be stored will be difference between j,i and minimum of elements of j,i
Step 3: The movement of i and j will be dependent on the next heightest pole

Time Complexity : O(n), as we are iterating the pole list once
Space Complexity : O(1), as we are using constant space
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, store = 0, len(height)-1, 0
        while i<j:
            store = max(store, (j-i)*min(height[i], height[j]))
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return store
