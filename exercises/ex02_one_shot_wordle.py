"""EX02 - one-shot wordle :0."""

__author__ = "730578652"

secret_word: str = "python"

# declaring all of my variables

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

check_idx: int = 0
altcheck_idx: int = 0
guess_track: str = ""
character_existence: bool = False

guessed_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

# while loop for checking if the length of the guessed word is the same as the length of the secret word - if not, try again
while len(guessed_word) > len(secret_word) or len(guessed_word) < len(secret_word):
    guessed_word = str(input(f"That was not {len(secret_word)} letters! Try again: "))

# checking each index in both the secret and guessed words, printing and storing a green box in guess_track if they match
while check_idx < len(secret_word):
    if guessed_word[check_idx] == secret_word[check_idx]:
        guess_track = guess_track + green_box
    else:
        # while a character is in the guessed word that is also in the secret word and the alternate check is less than the length of the secret word... checking if the indexes match or not, then indicing (either resulting in a yellow or white box for the current index)
        while character_existence is not True and altcheck_idx < len(secret_word):
            if guessed_word[check_idx] == secret_word[altcheck_idx]:
                character_existence = True
            else:
                altcheck_idx = altcheck_idx + 1
        if character_existence is True:
            guess_track = guess_track + yellow_box
        else:
            guess_track = guess_track + white_box
    check_idx = check_idx + 1
    character_existence = False
    altcheck_idx = 0
# printing the actual wordle guesses
print(guess_track)

if guessed_word == secret_word:
    print("Woo! You got it! ")
if len(guessed_word) == len(secret_word) and guessed_word != secret_word:
    print("Not quite. Play again soon! ")