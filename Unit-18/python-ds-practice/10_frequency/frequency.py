def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    search_count = 0

    for num in lst:
        if num == search_term:
            search_count +=1
    return search_count
