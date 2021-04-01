def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # initialize var for count = 0; every time a greater num is followed count will increase 
    count = 0 
    # first loop; len(nums) 
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            # if inner loop is greater than outer loop
            if nums[y] - nums[x]:
                count += 1 
    # return count 
    return count 
