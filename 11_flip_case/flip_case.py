def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # initialize flipped_phrase as empty str 
    flipped_phrase = '' 
    # .lower() on to_swap 
    to_swap = to_swap.lower() 

    # for in loop 
    for letter in phrase:
        if letter.lower() == to_swap:
            # .swapcase() method
            letter = letter.swapcase() 
        flipped_phrase += letter 
    return flipped_phrase 

