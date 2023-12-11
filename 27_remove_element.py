# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# Both solutions use the method of two pointers starting at the beginning of an array and moving towards the end of an array
# Pointer i is the fast-runner looping through the array one step at a time
# while pointer k is the slow-runner keeping track of the position of the next element to put into the array.

# Notes:
## Order doesn't matter
## Put all elements NOT EQUAL to val at the beginning of the array
## After that, other elements don't matter, even though there are some elements equal to val

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k

        # 1st: [0*,1,2,2,3,0,4,2] i = 1, k = 1
        # 2nd: [0,1*,2,2,3,0,4,2] i = 2, k = 2
        # 3rd: [0,1,2*,2,3,0,4,2] i = 3, k = 2
        # 4th: [0,1,2,2*,3,0,4,2] i = 4, k = 2
        # 5th: [0,1,2,2,3*,0,4,2] i = 5, k = 2
        # 6th: [0,1,3,2,3,0*,4,2] i = 6, k = 3
        # 7th: [0,1,3,0,3,0,4*,2] i = 7, k = 4
        # 8th: [0,1,3,0,4,0,4,2*] i = 8, k = 5

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k