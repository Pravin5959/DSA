'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the 
remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would 
you change your code?

Explanation: This question requires understanding of Two Pointers
Step1 : We need to check if subsequence s exists in t or not, as order matters we will initialize i, j two pointers
Step2 : We will iterate the t string with j pointer and if one by one checks if char in s is present in t or not, important to note is that until we get the current char we will
        not move the i to follow subsequence logic
Step3 : Finally, if i becomes len(s) then it is a subsequence else no

Time Complexity = O(n), as we are iterating both the string at max it can be n+n = 2n
Space Complexity = O(1), as we are using constant space
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return True if i==len(s) else False
