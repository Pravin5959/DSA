'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

Explanation: This problem checks your knowledge on GCD and string comparition
Step1 : As we know that the GCD length of characters will be the string if at all both the string satisifes the coondition of s = n*t
        where s -> string, n -> total number of time its concatenated and t -> substring or gcd length string, we will compute gcd
Step2 : Once, gcd is computed next step is to check the validity of strings, which can be easily checked in two following ways:
        -- Split both the string based on the gcd length and put the elements in two different set and check if the length of sets is
           1 and both the sets are equal or not
        -- Just check if str1 + str2 == str2 + str1 or not

Time Complexity : O(n), where n is the length of smaller string
Space Complexty : O(1), as we are not using any structure
'''
class Solution:
    def getGDC(self, int1: int, int2: int) ->int:
        min_val, gcd= int1 if int1 < int2 else int2, 1
        for i in range(1, min_val+1):
            if(int1 % i == 0 and int2 % i == 0):
                gcd = i
        return gcd
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = self.getGDC(len(str1), len(str2))
        return str1[0:gcd] if str1 + str2 == str2 + str1 else ''
