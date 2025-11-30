# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Nothing to merge
        if n == 0:
            return nums1
        
        if m == 0:
            nums1[:] = nums2
            return nums1

        # Initialize pointers
        p1 = 0
        p2 = 0

        # Initialize empty array
        merged_array = []

        # Main Loop. While both arrays have elements ...
        while p1 < m and p2 < n:
            
            if nums1[p1] <= nums2[p2]:
                merged_array.append(nums1[p1])
                p1 += 1
            else:
                merged_array.append(nums2[p2])
                p2 += 1

        # Copy remaining elements
        while p1 < m:
            merged_array.append(nums1[p1])
            p1 += 1

        while p2 < n:
            merged_array.append(nums2[p2])
            p2 += 1

        # Store the result back in nums1
        nums1[:] = merged_array

        return nums1
