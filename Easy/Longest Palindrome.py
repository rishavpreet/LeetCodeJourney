'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.



Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        def check_for_odd(hm: dict):
            for val in hm.values():
                if val % 2 == 1:
                    return True
            return False

        hm = {}
        if len(s) == 0:
            return 0
        max_pal = 0
        for l in s:
            if hm.get(l) is not None:
                hm[l] += 1
                if hm[l] % 2 == 0:
                    max_pal += 2
            else:
                hm[l] = 1
        if check_for_odd(hm):
            max_pal += 1
        return max_pal
