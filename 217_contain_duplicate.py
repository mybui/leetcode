# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for i in nums:
            if i in existed:
                return True
            existed.add(i)
        return False