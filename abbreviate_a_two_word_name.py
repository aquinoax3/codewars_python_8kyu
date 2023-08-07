# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F


def abbrev_name(name):
    list = name.split(" ")

    return list[0][0].upper() + "." + list[1][0].upper()
