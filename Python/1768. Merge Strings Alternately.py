'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Explanation: This problem checks your undrerstanding your string indexing and iterables technique
Step1 : If the string are of same length then we need to iterate over the string length and concatenate characters one by one
Step2 : If the string are of not same length, we need to consider smaller string's length for iterating and concatenating, further
        we need to just attach the left out part of the bigger string's character

Time Complexity : The TC is O(n), where n is the length of the larger string
Space Complexity : The SC is O(1), as we are not using any specific structure
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op, rng = '', min(len(word1), len(word2))
        attch = word1[rng:] if len(word1) > len(word2) else word2[rng:] if len(word1) < len(word2) else ''
        for itr in range(rng):
            op = ''.join([op, word1[itr], word2[itr]])
        return ''.join([op,attch])
