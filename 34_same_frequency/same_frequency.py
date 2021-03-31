def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # return frequency_num 
    return frequency_num(str(num1)) == frequency_num(str(num2))

# new function 
def frequency_num(x):
# initialize empty dictionary
    dictionary_count = {} 
# for in loop 
    for num in x:
        dictionary_count[num] = dictionary_count.get(num, 0) + 1
    return dictionary_count 