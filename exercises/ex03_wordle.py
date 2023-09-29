"""EX03 - wordle!"""

__author__ = "730578652"

def contains_char(search_for_parameter: str, search_char: str) -> bool:
    """Function meant to see if an entered character is found in an entered word at any index."""
    assert len(search_char) == 1                                                                    # making sure that the length of parameter 2 (search_char) is 1/a single character
    
    check_idx: int = 0                                                                              # initializing the index checker to 0
    
    while check_idx < len(search_for_parameter):                                                    # while the current index check is less than the length of the first parameter...
        if search_for_parameter[check_idx] == search_char:                                          # if the current index check is equal to the entered character...
            return True
        check_idx = check_idx + 1                                                                   # moving on to the next index if the current index is not equal to the enterd character
    return False                                                                                    # if the entered character is not in the first parameter at all

def emojified(guess: str, secret_word: str) -> str:
    """Function meant to return a str with colored emojis to test closeness of a guessed word and a secret stored word."""
    assert len(guess) == len(secret_word)                                                           # making sure that the length of the guessed word is the same as the length of the secret word

    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    result: str = ""                                                                                # the result that is printed after a guess; storage for the emojis
    check_idx: int = 0                                                                              # initializing the index checker to 0

    while check_idx < len(secret_word):                                                             # while the current index check is less than the length of the secret word...
        if contains_char(secret_word, guess[check_idx]) is True:                                    # if the function "contains_char" with the entered guess and secret_word parameters is true (since contains_char will return a bool)
            if guess[check_idx] == secret_word[check_idx]:                                          # if the indexes of the two parameters match...
                result = result + green_box                                                         # return a green box, which indicates that the current indexes match in both parameters, and initlialize it to that index in the return string
            else:
                result = result + yellow_box                                                        # if the current index of the two parameters is not the same, but a character exists in the word, return a yellow box and initialize it to that index in the return string
        if contains_char(secret_word, guess[check_idx]) is False:                                   # if the function "contains_char" with the entered guess and secret_word paramters is not false (no characters matching)...
            result = result + white_box                                                             # return a white box and initialize it to the return string
        check_idx = check_idx + 1                                                                   # check for the next index
    return result                                                                                   # return the result string after checking all of the indexes of the parameters!

def input_guess(expected_length: int) -> str:
    """Function meant to prompt the user to enter a word of a specific number of characters."""
    expected_guess: str = input(f"Enter a {expected_length} character word: ")                      # the variable "expected_guess" is defined as a string that you get from the question "enter a _ character word", with the integer coming from the parameter "expected_length"
    
    while len(expected_guess) != expected_length:                                                   # when the length of the expected_guess/perviously defined integer is not the length of the expected_length parameter...
        expected_guess = (input(f"That wasn't {expected_length} chars! Try again: "))               # prompt the user to input another guess that should contain the correct amount of characters
    return expected_guess                                                                           # after the while loop is complete (aka once the user inputs a guess that is the correct amount of characters), return the proper expected_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"                                                                      # the secret word that the user is trying to guess
    turn_number: int = 1                                                                            # variable to keep track of the turn number for the user

    while turn_number <= 6:                                                                         # turn number has to be less than or equal to six because the user only gets six guesses
        print(f"=== Turn {turn_number}/6 ===")                                                      # the printed statement letting the user know what turn number they are on
        guess: str = input_guess(len(secret_word))                                                  # from function input_guess, checking to make sure the guessed word is the correct amount of characters, and if it is, initializing it as a string
        print(emojified(guess, secret_word))                                                        # from emojified, printing the guessed word's emojis - showing if they are in the correct of incorrect places in the secret word
        if guess == secret_word:                                                                    # if the guess is actually the secret word/if they guess correctly...
            print(f"You won in {turn_number}/6 turns!")                                             # printing a congrats statement
            return None                                                                             # closing out main
        turn_number = turn_number + 1                                                               # to add on a turn number after every user guess
        if turn_number > 6:                                                                         # if the user has not gotten the guess in six...
            print("X/6 - Sorry, try again tomorrow!")                                               # printing a failure statement
            return None                                                                             # closing out main
        
if __name__ == "__main__":
    main()                                                                                          # running main...