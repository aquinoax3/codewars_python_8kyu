# Your task is simply to count the total number of lowercase letters in a string.

# Examples
# "abc" ===> 3

# "abcABC123" ===> 3

# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

# "" ===> 0;

# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

# "abcdefghijklmnopqrstuvwxyz" ===> 26


import re


def lowercase_count(strng):
    match = re.findall("[a-z]", strng)

    return len(match)



print(lowercase_count("abc"), 3)