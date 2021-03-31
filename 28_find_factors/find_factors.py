def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    # num % i == 0 
    total = [] 
    # using outside code 
    for i in range(1, num + 1):
    # remainder should be equal to 0 
        if num % i == 0:
    # add i to total list 
            total.append(i) 
    # return full list 
    return total 