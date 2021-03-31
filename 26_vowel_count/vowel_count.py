def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # start with vowels 
    vowels = ['a', 'e', 'i', 'o', 'u']
    # dictionary_count {} 
    dictionary_count = {} 
    # phrase to lower case 
    low_phrase = phrase.lower()
    # iterate letter in low_phrase 
    for letter in low_phrase: 
    # if letter in vowels 
        if letter in vowels:
            dictionary_count[letter] = dictionary_count.get(letter, 0) + 1 
    # return 
    return dictionary_count 

