'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

Explanation : This problem requires understanding of counters and dictionary in data structures

Step1 : As we know in 2 scenarios it will not satisfy the conditions i.e.length of strings being different or any different keys are present in anyone of the string
Step2 : To find if any different key is present, we are creating a counter out of the strings, through which by comparision we can say if any key is different
Step3 : If all of the conditions are satisified above, we finally need to check the swapping scenario by checking of count of occurances are similar across the values of counters

Time complexity:
O(n), as we are iterating the strings at max n+n+constant=2n

Space complexity:
O(1), in all the scenrios I think we will never exceed more than 26 elements storage, it's doubtable
'''
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if len(word1) != len(word2) or cnt1.keys() != cnt2.keys():
            return False
        else:
            return True if Counter(cnt1.values()) == Counter(cnt2.values()) else False
