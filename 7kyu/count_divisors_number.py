import math

def divisors(n):
    count = 0
    # Iterate up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If i is a divisor
            count += 1  # Count divisor i
            if i != n // i:  # If i and n//i are distinct, count n//i as well
                count += 1
    return count
