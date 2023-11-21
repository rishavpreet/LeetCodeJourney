'''
Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1
        if not s:
            return 0
        left = 0
        seen = {}
        i = 0
        for i in range(len(s)):
            if seen.get(s[i]) is None:
                max_len = max(i - left + 1, max_len)
            else:
                if seen[s[i]] < left:
                    max_len = max(i - left + 1, max_len)
                else:
                    left = seen[s[i]] + 1
            seen[s[i]] = i
        return max_len
