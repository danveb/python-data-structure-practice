def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # initialize empty counter {}
    counter = {}
    # for in loop
    for num in nums: 
        counter[num] = counter.get(num, 0) + 1 
    # find frequent number 
    max_num = max(counter.values())
    # check index 
    for (num, frequency) in counter.items():
        # if frequency is max_num 
        if frequency == max_num:
            # return num! 
            return num 