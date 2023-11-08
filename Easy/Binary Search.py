''''''

from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + floor((hi - lo) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    output = 3
    result = sol.search(nums=nums, target=target)
    print(result)
    assert output == result
