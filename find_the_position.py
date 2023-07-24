# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"


def position(alphabet):
    letters = "abcdefghijklmnopqrstuvwxyz"

    for char in range(len(letters)):
        if letters[char] == alphabet:
            return f"Position of alphabet: {char + 1}"
