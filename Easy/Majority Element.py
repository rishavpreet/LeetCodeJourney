'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
 always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
from typing import List


# using hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n_len = len(nums)
        if n_len == 1:
            return nums[0]
        for n in nums:
            if hm.get(n) is not None:
                hm[n] += 1
                if hm[n] > n_len / 2:
                    return n
            else:
                hm[n] = 1


# using moore's voting algorithm

class SolutionTwo:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                count += 1
                majority = n
            elif majority == n:
                count += 1
            else:
                count -= 1
        return majority
