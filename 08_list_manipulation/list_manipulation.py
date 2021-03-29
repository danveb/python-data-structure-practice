def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    # remove
    # lst = [1,2,3] 
    # if statement 
    if command == 'remove':
        if location == 'end':
            # removes last item of list
            return lst.pop() 
        elif location == 'beginning':
            # removes first item of list using .pop(0 index) 
            return lst.pop(0)

    # add 
    # lst = [1,2,3] 
    elif command == 'add':
        if location == 'beginning':
            # add 20 to beginning of list 
            # use insert(index, x)
            lst.insert(0, value)
            return lst
        elif location == 'end':
            # add 30 to end of list 
            # use .append(x) to end of list 
            lst.append(value)
            return lst 

