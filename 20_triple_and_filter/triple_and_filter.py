def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # use list comprehension for % 4 == 0 
    # return [num * 3 for num in nums if num % 4 == 0]

    # OR another solution? 
    # initialize empty list to append later on 
    new_list = [] 
    # for in loop over existing list 
    for num in nums:
    # if % 4 == 0 
        if num % 4 == 0:
    # append to new_list    
            new_list.append(num * 3)  
    # return new_list 
    return new_list 