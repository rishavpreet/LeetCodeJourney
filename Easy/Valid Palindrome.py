'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

'''
import re
from math import floor

pattern = re.compile('[\W_]+')


# with regex
class SolutionOne:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = pattern.sub("", s)
        s_len = len(s)
        # print(s_len)
        if s_len % 2 == 0:
            # print(s[0:floor(s_len/2)],s[s_len-1:floor(s_len/2)-1:-1])
            if s[0:floor(s_len / 2)] == s[s_len - 1:floor(s_len / 2) - 1:-1]:
                return True
            else:
                return False
        else:
            # print("else",s[0:floor(s_len/2)], s[s_len-1:floor(s_len/2):-1])
            if s[0:floor(s_len / 2)] == s[s_len - 1:floor(s_len / 2):-1]:
                return True
            else:
                return False


## with isalnum
class SolutionTwo:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([i if i.isalnum() else "" for i in s])
        s_len = len(s)
        print(s_len, s)
        if s_len % 2 == 0:
            # print(s[0:floor(s_len/2)],s[s_len-1:floor(s_len/2)-1:-1])
            if s[0:floor(s_len / 2)] == s[s_len - 1:floor(s_len / 2) - 1:-1]:
                return True
            else:
                return False
        else:
            # print("else",s[0:floor(s_len/2)], s[s_len-1:floor(s_len/2):-1])
            if s[0:floor(s_len / 2)] == s[s_len - 1:floor(s_len / 2):-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    sol = SolutionTwo()
    s = "A man, a plan, a canal: Panama"
    output = True
    result = sol.isPalindrome(s=s)
    print(result)
    assert output == result
