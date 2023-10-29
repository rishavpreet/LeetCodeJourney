'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].


'''


# using list
class SolutionOne:
    def romanToInt(self, s: str) -> int:
        sym_map = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}
        sub_map = {
            5: 4,
            50: 40,
            500: 400,
            10: 9,
            100: 90,
            1000: 900
        }
        num_list = []
        idx_op = 0
        for idx, c in enumerate(s):
            print(c, idx, num_list, sum(num_list))
            idx = idx - idx_op
            if idx > 0:
                print(f"{num_list[idx - 1]} < {sym_map[c]}")
                cr = num_list[idx - 1]
                if cr < sym_map[c]:
                    num_list.pop()
                    print(cr)
                    num_list.append(sub_map[sym_map[c]])
                    idx_op += 1
                else:
                    num_list.append(sym_map[c])
            else:
                num_list.append(sym_map[c])
        print(num_list)
        return sum(num_list)


# without list
class SolutionTwo:
    def romanToInt(self, s: str) -> int:
        sym_map = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}
        sub_map = {
            5: 4,
            50: 40,
            500: 400,
            10: 9,
            100: 90,
            1000: 900
        }
        sub_count = 0
        prev_num = None
        num = 0
        for idx, c in enumerate(s):
            idx = idx - sub_count
            if idx > 0:
                if prev_num < sym_map[c]:
                    num = num - prev_num + sub_map[sym_map[c]]
                    sub_count += 1
                else:
                    num += sym_map[c]
            else:
                num += sym_map[c]
            prev_num = sym_map[c]
        return num


if __name__ == '__main__':
    sol = SolutionTwo()
    s = "MCMXCIV"
    output = 1994
    result = sol.romanToInt(s=s)
    print(result)
    assert output == result
