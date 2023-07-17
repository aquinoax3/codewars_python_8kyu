# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


# cleaner solution
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# first solution
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
