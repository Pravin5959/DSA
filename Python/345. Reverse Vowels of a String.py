'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Explanation: This question requires understanding on two pointers approach in algorithms
Step1 : Assign two pointers one with right movement from 0 and second with left movement from end of list
Step2 : Keep on moving the poiners until we encounter any charachter which is a vowel from both the sides
Step3 : Based upon step2 result we need to swap the character at each pointers
Step4 : While performing all the above steps we should be taking care of indexing not going out of range

Time Complexity : O(n), as we are traversing the list once
Space Complexity : O(n), as strings are immutable in python, for swapping we are storing data in a list
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels_lst = ['a', 'e', 'i', 'o', 'u']
      str_lst = list(s)
      i, j = 0, len(str_lst) - 1
      while i < j:
        while i < j and str_lst[i].lower() not in vowels_lst : i += 1
        while i < j and str_lst[j].lower() not in vowels_lst : j -= 1
        if i<=j: str_lst[i], str_lst[j] = str_lst[j], str_lst[i]
        i, j = i + 1, j - 1
      return ''.join(str_lst)
