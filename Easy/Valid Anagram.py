'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
        for j in t:
            if j in t_map:
                t_map[j] += 1
            else:
                t_map[j] = 1
        return s_map == t_map


if __name__ == '__main__':
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    output = True
    result = sol.isAnagram(s=s, t=t)
    print(result)
    assert output == result
