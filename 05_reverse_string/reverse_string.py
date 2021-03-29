def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # use slicing; empty start, end, step -1 to reverse 
    return phrase[::-1] 
