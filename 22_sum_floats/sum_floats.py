def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    
    # total = 0 
    total = float(0)  
    # for in loop 
    for num in nums: 
    # if isinstance(num, float) 
        if isinstance(num, float): 
    # total += num 
            total += num 
    # return total 
    return total 

    # Another solution? use list comprehension 
    # [for num in nums]
    # [if instance(num, float)] -> checks for num is float
    # [num] 
    # get the sum([]) 
    return sum([num for num in nums if isinstance(num, float)]) 
