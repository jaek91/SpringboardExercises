def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    res = all(isinstance(el,list) for el in lst)

    if res:
        return True
    else: 
        return False




