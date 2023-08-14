# Solution 1 and solution 2 are two ways of comparing nums1 and nums2
# Solution 1 checks for the case nums1 lte nums 2
# Solution 2 checks for the case nums1 gte nums 2

class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # backfilling because arrays are already in sorted order
        # last position of nums1
        last = m + n - 1
        # nums1 index
        i = m - 1
        # nums2 index
        j = n - 1

        # start at the last REAL numbers of both arrays
        # while there exist REAL numbers in nums1 to be modified
        while i >= 0:
            # if (the current number of) nums1 is lte to (the current number of) nums2,
            # and there exist REAL numbers in nums2 to compare
            # replace nums2 into nums1
            if j >= 0 and nums1[i] <= nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
            # else (if the current number of nums1 is gte to nums2,
            # or there doesn't exist any REAL numbers in nums2 to compare anymore)
            # replace nums1 into nums1
            else:
                nums1[last] = nums1[i]
                i -= 1
            last -= 1
        
        # while there doesn't exist any REAL number in nums1 to be modified
        # and there exist REAL numbers in nums2 to compare
        while i < 0 and j >= 0:
            # replace nums2 into nums1
            nums1[last] = nums2[j]
            last -= 1
            j -= 1

class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # backfilling because arrays are already in sorted order
        # last position of nums1
        last = m + n - 1
        # nums1 index
        i = m - 1
        # nums2 index
        j = n - 1

        # start at the last REAL numbers of both arrays
        # while there exist REAL numbers in nums2 to compare
        while j >= 0:
            # if (the current number of) nums1 is gte to (the current number of) nums2,
            # and there exist REAL numbers in nums1 to be modified
            # replace nums1 into nums1
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            # else (if the current number of nums1 is lt nums2,
            # or there doesn't exist any REAL numbers in nums1 to be modified anymore)
            # replace nums2 into nums1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1