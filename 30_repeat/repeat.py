def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    # comprehension? 
    list = [char * 3 for char in phrase]
    # using map method to map str (convert elements in list to str) 
    list_to_str = ' '.join(map(str, list)) 
    return list_to_str 