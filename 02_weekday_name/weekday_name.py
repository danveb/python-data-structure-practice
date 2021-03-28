def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # create list of DAYS
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
    # if statement (less than 1 & greater than 7)
    if day_of_week < 1 and day_of_week > 7:
        return None
    # use index of list to return correct day -1 
    return days[day_of_week -1]