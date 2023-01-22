#  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List

""" циклическая сортировка!!!"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # new_list = []
        # for i in range(1, n+1):
        #     if i not in nums:
        #         new_list.append(i)
        # return new_list
        i = 0
        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1

        new_list = []
        for k in range(len(nums)):
            if nums[k] != k+1:
                new_list.append(k+1)
        return new_list



s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
