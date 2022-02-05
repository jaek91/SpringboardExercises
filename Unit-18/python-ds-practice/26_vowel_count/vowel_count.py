def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    edited_phrase = phrase.replace(" ", "").lower()
    vowel_count = {}.fromkeys('aeiou',0)
    for char in edited_phrase:
        if char in vowel_count:
            vowel_count[char] += 1
    return vowel_count

