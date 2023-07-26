# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.


def find_average(numbers):
    if len(numbers) == 0:
        return 0

    sum = 0

    for num in numbers:
        sum += num

    return sum / len(numbers)
