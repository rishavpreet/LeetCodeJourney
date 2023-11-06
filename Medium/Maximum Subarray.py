'''
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

'''
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        cur_sum = 0
        cur_array = []
        start_ind = 0
        end_ind = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if max_sum < cur_sum:
                max_sum = cur_sum
                end_ind = i + 1
            if cur_sum < 0:
                cur_sum = 0
                start_ind = i + 1

            print(nums[start_ind:end_ind])
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 2, 1, -5, 4]
    output = 4
    result = sol.maxSubArray(nums=nums)
    print(result)
    assert output == result
