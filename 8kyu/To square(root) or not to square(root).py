import math

def square_or_square_root(arr):
    result = []
    for number in arr:
        # Calculate the integer square root of the number
        sqrt = math.isqrt(number)
        # Check if squaring the integer square root returns the original number
        if sqrt * sqrt == number:
            result.append(sqrt)
        else:
            result.append(number * number)
    return result