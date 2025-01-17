# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.



My Solution :
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j


# It works but not time efficient as it contains two for loops

# Optimal Solution:
# *use hash map to traverse only once

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for ind,num in enumerate(nums):
            diff=target-num
            if diff in prev:
                return [prev[diff],ind]
            prev[num]=ind
