'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true



Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        if len(magazine) < len(ransomNote):
            return False

        for l in magazine:
            if hm.get(l) is not None:
                hm[l] += 1
            else:
                hm[l] = 1
        print(hm)

        for l in ransomNote:
            if hm.get(l) is not None and hm[l] > 0:
                hm[l] -= 1
            else:
                return False

        return True
