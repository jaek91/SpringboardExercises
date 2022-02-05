def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    final = []
    for el in lst:
        if bool(el):
            final.append(el)
    return final

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))