'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

'''
from typing import List


## Brute Force
class SolutionOne:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for idx, j in enumerate(nums):
                if nums[i] + j == target and i != idx:
                    return [i, idx]


## HashMap
class SolutionTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = dict()
        for idx, j in enumerate(nums):
            if ht.get(target - j) is not None:
                return [ht.get(target - j), idx]
            ht[j] = idx


if __name__ == '__main__':
    sol = SolutionOne()
    nums = [2, 7, 11, 15]
    target = 9
    output = [0, 1]
    assert output == sol.twoSum(nums=nums, target=target)
