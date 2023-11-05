'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
import operator
from itertools import accumulate
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, n = list(accumulate(nums, operator.mul)), list(accumulate(nums[::-1], operator.mul))[::-1], len(nums)
        result = []
        for i in range(n):
            pre_mul = (pre[i - 1] if i else 1)
            suf_mul = (suf[i + 1] if i + 1 < n else 1)
            result.append(pre_mul * suf_mul)
        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    result = sol.productExceptSelf(nums=nums)
    print(result)
    assert output == result
