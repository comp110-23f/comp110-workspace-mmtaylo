"""ex01_chardle - baby steps toward Wordle."""

__author__ = "730578652"

# defining the constant correct_characters
correct_characters: int = 0

guessed_word: str = input("Enter a 5-character word: ")

# error message if guessed_word != 5 characters
if len(guessed_word) != 5:
    print("Error: Word must contain 5 characters. Try again, please.")
    exit()

guessed_character: str = input("Enter a single character: ")

# error message of guessed_character != a single character
if len(guessed_character) != 1:
    print("Error: Character must be a single character. Try again, please.")
    exit()

# buffer message (if the previous two conditions are satisfied)
print("Searching for " + guessed_character + " in " + guessed_word)

# defining if there are guessed_characters in guessed_word
if guessed_character == str(guessed_word[0]):
    print(guessed_character + " found at index 0")
    correct_characters = correct_characters + 1

if guessed_character == str(guessed_word[1]):
    print(guessed_character + " found at index 1")
    correct_characters = correct_characters + 1

if guessed_character == str(guessed_word[2]):
    print(guessed_character + " found at index 2")
    correct_characters = correct_characters + 1

if guessed_character == str(guessed_word[3]):
    print(guessed_character + " found at index 3")
    correct_characters = correct_characters + 1

if guessed_character == str(guessed_word[4]):
    print(guessed_character + " found at index 4")
    correct_characters = correct_characters + 1

# defining the amount of correct_characters in guessed_character
if correct_characters < 1:
    print("No instances of " + guessed_character + " in " + guessed_word)

if correct_characters == 1:
    print("1 instance of " + guessed_character + " in " + guessed_word)

if correct_characters >= 2:
    print(str(correct_characters) + " instances of " + guessed_character + " in " + guessed_word)