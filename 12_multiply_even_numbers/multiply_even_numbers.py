def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # initialize total as 1
    total = 1 
    # for in loop on nums 
    for num in nums:
    # -- if x % 2 == 0 
        if num % 2 == 0: 
    # ---- total to equal total * num 
            total *= num 
    # return total 
    return total 
    # no need to check for odd numbers since we already get total = 1 
    