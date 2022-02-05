
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    final_dict = {}

    for ltr in phrase:
        final_dict[ltr] = final_dict.get(ltr, 0) + 1
    
    return final_dict
    
print(multiple_letter_count("hello world"))

