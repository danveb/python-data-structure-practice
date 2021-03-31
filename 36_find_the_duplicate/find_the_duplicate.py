def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # # initialize empty list for duplicate_list
    # duplicate_list = [] 
    # # initialize a counter to count on number of duplicates
    # counter = 0 
    # # iterate for each_element in nums list 
    # # if nums.count(each_element) 

    # initialize counter at 0 
    counter = 0
    # num = nums[0] 
    num = nums[0] 
    # iterate val in nums 
    for val in nums: 
    # current_freq will be equal to nums.count(val) 
        current_freq = nums.count(val) 
    # if current_freq is > counter
        if current_freq > counter: 
    # counter is equal to current_freq 
            counter = current_freq
    # num = i 
            num = val 
    # return num 
    return num 
