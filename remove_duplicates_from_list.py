# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.


def distinct(seq):
    result = []

    for num in seq:
        if num not in result:
            result.append(num)

    return result
