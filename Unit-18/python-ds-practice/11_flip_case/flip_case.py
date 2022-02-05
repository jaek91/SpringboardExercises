def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    final = ""
    for char in phrase:
        if char == to_swap:
            final += char.swapcase()
        elif char.upper() == to_swap:
            final += char.swapcase()
        elif char.lower() == to_swap:
             final += char.swapcase()
        else:
            final += char
    return final

print(flip_case('Aaaahhh', 'h'))

