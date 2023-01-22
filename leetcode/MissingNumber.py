#  https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # new_list = [x for x in range(len(nums) + 1)]
        # for i in new_list:
        #     if i not in nums:
        #         return i
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


s = Solution()
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
