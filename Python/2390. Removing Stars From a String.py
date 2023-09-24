'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

Explanation : This problem requires basic understanding of stack in data structures
Stack : It is a data structure which follows LIFO mechanism to perform its storage and operation:
push() -> Pushes the element in the stack
pop() -> Remove last element added in the stack
top() -> Returns the last element in the stack
empty() -> Returns flag based on stack size, if empty then true

Step1 : As per the problem, we need to treat the * in the string input as 'BACKSPACE' in keyboard based on which we need to return the final output
Step2 : We will add the element in the stack until * comes while iterating, for * we will just keep on popping the elements from the stack, as per the problem we will never face any execptions

Time complexity:
O(n), as we are iterating the list at max n+n=2n times

Space complexity:
O(n), as we are using stack data structure which stores at max n elements
'''
from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for char in s:
            if char == '*': stack.pop()
            else: stack.append(char)
        return ''.join(stack)
