'''
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"



Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
'''


## brute force basic approach

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def remove_zeroes(r: str) -> str:
            i = 0
            for i in range(len(r)):
                # print("rz",r[i], i)
                if r[i] != '0':
                    break
                else:
                    continue
            return r[i:]

        result = ""
        carry = 0

        for i in range(0, max(len(a), len(b)) + 1):
            try:
                s1 = int(a[-i - 1])
            except:
                s1 = 0
            try:
                s2 = int(b[-i - 1])
            except:
                s2 = 0
            print(s1, s2, carry)
            r = s1 + s2 + carry
            if r <= 1:
                carry = 0
            elif r == 2:
                carry = 1
                r = 0
            else:
                carry = 1
                r = 1
            result += str(r)
            print(result)
        return remove_zeroes(result[::-1])


## optimised method
class SolutionTwo:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(a[i]) - ord('0')

            if j >= 0:
                sum += ord(b[j]) - ord('0')

            i, j = i - 1, j - 1

            carry = 1 if sum > 1 else 0

            result += str(sum % 2)

        if carry != 0:
            result += str(carry)
        return result[::-1]
