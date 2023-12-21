# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# The solution uses the method of two pointers starting at the beginning of an array and moving towards the end of an array.
# Pointer j is the fast-runner looping through the array one step at a time,
# while pointer i is the slow-runner keeping track of the position of the current deduplicated element.

# Notes:
# The input list has already been SORTED.
# Put all deduplicated elements at the beginning of the array
# After that, other elements don't matter, even though there are some duplicated elements.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1

        # j = 9, nums = [0, 0->1, 1->2, 1->3, 1i->4, 2, 2, 3, 3, 4j], output = [0, 1, 2, 3, 4]
