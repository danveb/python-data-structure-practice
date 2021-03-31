def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # use isinstance to check if list 
    # iterate over main list and check each item 
    for each_item in lst:
    # if not isinstance(x, list) 
        if not isinstance(each_item, list):
    # return false 
            return False 
    # else return true 
    return True 


