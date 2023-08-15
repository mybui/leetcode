# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# notes:
## order doesn't matter
## put all elements not equal to val at the beginning of the array
## after that, the elements don't matter even though there are some equal to val

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