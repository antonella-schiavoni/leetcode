# https://leetcode.com/problems/rotate-array/description/

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    # 1. Handle the modulo operation
    n = len(nums)
    if n == 0:
        return # Cannot rotate an empty array

    k = k % n # Ensure that the rotation algorithm only runs for the minimum necessary number of steps

    # 2. Slice and Concatenate
    # Part 1: The last k elements (the new beginning)
    part_two = nums[-k:]

    # Part 2: The first n-k elements (the new end)
    part_one = nums[:-k]

    # 3. Assemble the new array
    new_array = part_two + part_one

    # Since the problem typically asks for an in-place modification, 
    # you must copy the new array back into the original nums list:
    nums[:] = new_array 
        
