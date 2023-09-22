'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5

Explanation : This problem requires the understanding of dictionary and matrix elements iteration

Step1 : As we need to compare the row elements with column elements, we are first mapping the occurances of rows in a dictionary
Step2 : We are then iterating the column elements in the list and checking if it is present in the row dictionary, based upon which we are adding up the result

Time complexity:
O(n^2), the first iteration is taking n^2 where first n is for iteration over the row and second if for the str, the second iteration is taking n*3(n), so overall it is O(n^2)

Space complexity:
O(n^2), at max we are storing all the elements in the provided grid
'''
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, dct = 0, defaultdict(int)
        for row in grid: dct[str(row)] += 1
        for idx in range(len(grid)):
            col = []
            for jdx in range(len(grid)):
                col.append(grid[jdx][idx])
            if str(col) in dct.keys():
                res += dct[str(col)]
        return res
