'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Explanation: This question requires undertanding of fast and slow pointer
Step1 : In this problem the most important part is to understand where to store what (globally and locally)
Step2 : Globally we are storing fast moving pointer which will count the occurances of characters and slow moving pointer which will
        update the compression values accordingly
Step3 : Interally we are storing two variables storer and cnt, were storer will store the current iterating character and cnt will
        count the occurance of that character
Step4 : Finally based upon the problem we are storing the compressed data

Time complexity : O(n), as we are traversing the list at max  n+n = 2n times,
Space complexity : Its debatable, as we are storing and iterating the value in list, still it seems O(1) as it will never par number
                    of digits of max length the input array can have
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast<len(chars):
            storer, cnt = chars[fast], 0
            while fast<len(chars) and storer == chars[fast]:
                cnt, fast = cnt+1, fast+1
            if slow<len(chars):
                chars[slow] = storer
                slow += 1
                if cnt == 1: continue
                else:
                    for i in list(str(cnt)):
                        chars[slow] = i
                        slow += 1
        return slow
