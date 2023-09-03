# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata


def shortcut(s):
    result = ""

    for char in s:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            result += char

    return result
