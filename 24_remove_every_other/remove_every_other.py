def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # ONLY WORKS ON 1,2,3,4,5 
    # Initialize empty list 
    every_other = [] 
    # for each_item in lst 
    for each_item in lst:
    # if each_item % 2 == 1 
        if each_item % 2 == 1:
    # every_other.append(each_item) (to add) 
            every_other.append(each_item)
    # return every_other 
    return every_other 

    # Maybe another solution? 
    # return lst[::2] 