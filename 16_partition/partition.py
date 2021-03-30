def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # initialize 2 lists; pass or fail 
    passed_test = [] 
    failed_test = [] 
    # for in loop 
    for item in lst:
        # if True 
        if fn(item):
            passed_test.append(item) 
        else:
            failed_test.append(item) 
    # return here 
    return [passed_test, failed_test] 