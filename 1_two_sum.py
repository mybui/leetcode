class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        count = dict()
        for i in range(len(nums)):
            c = target - nums[i]
            # if found the complement existed in the list
            # return the index of the complement in the list,
            # and the index of the current element
            if c in count:
                return [count[c], i]
            # else, continue making a map of list elements and indexes
            count[nums[i]] = i
        return []