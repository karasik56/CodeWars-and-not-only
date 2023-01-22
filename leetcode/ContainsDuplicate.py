#  https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) == len(set(nums)) else False
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4]))
