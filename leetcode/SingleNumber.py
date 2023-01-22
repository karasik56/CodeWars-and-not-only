#  https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # new_dict = {}
        # for num in nums:
        #     if new_dict.get(num):
        #         new_dict[num] += 1
        #     else:
        #         new_dict[num] = 1
        # for k, j in new_dict.items():
        #     if j == 1:
        #         return k
        mask = 0
        for num in nums:
            mask ^= num
        return mask


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
