"""CL04 practice writing functions."""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words
    # different ways to call the function mimic
    mimic("Hello!")

    print(mimic("Hello!"))

    my_words: str = "Hello!"
    response: str = mimic(my_words)
    print(response)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return ("Too high of an index.")
    # if we made it to here, that means that the letter_idx is valid
    return my_words[letter_idx]