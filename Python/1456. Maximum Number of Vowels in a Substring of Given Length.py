'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Explanation : This problem requires understanding of Sliding Window design pattern in algorithms
Step1 : As we need to check a fixed k length subarray, we need to make sure our pointers difference is k-1 elements
Step2 : To achieve that, we will use two pointers i, j where j will be moving at the end of the window anf i will be moving at 
        start of the window
Step3 : As the window will move forward after a fix length, we will make sure to remove the value which window is no more part of 
        based upon the element being a vowel or not, and will keep of checking the max value until the complete list is iterated

Time complexity:
O(n), as we are traversing the input list at max n+n = 2n times

Space complexity:
O(1), as we are using constant space
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j, glb_max, loc_sum, vowels = 0, 0, float('-inf'), 0, ['a', 'i', 'e', 'o', 'u']
        while j<len(s):
            loc_sum += 1 if s[j] in vowels else 0
            if j-i+1 == k:
                glb_max = max(glb_max, loc_sum)
                loc_sum -= 1 if s[i] in vowels else 0
                i += 1
            j += 1
        return glb_max
