'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Explanation : This problem requires very good understanding of stack data structure
Step1 : As we have three types of data present in the input string i.e. numerical, lower case alphabets and the square brackets, so in each scenario what should happen we need to put
Step2 : Whenever a '[' is coming then we need to store the till point calcualted string and number in the stack
Step3 : Whenever a ']' is coming, we need to compute based on the current string how many times it need to multiplied and what previous string needs to be concatenated
Step4 : Whenever a numeric charachter or lower case charachter is coming we need to append in the current string and current num variable

Time complexity:
O(n), as we are iterating the list only once and we are using int() for conversion from string to int
Space complexity:
O(n), as we are using stack + curString + curNum whoes max complexity can be 2n
'''
def decodeString(self, s: str) -> str:
        stack, curStr, curNum = [], '', ''
        for c in s:
            if c == '[':
                stack.append(curStr)
                stack.append(curNum)
                curStr, curNum = '', ''
            elif c == ']':
                prevNum = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + int(prevNum)*curStr
            elif c.isdigit():
                curNum += c
            else:
                curStr += c
        return curStr
