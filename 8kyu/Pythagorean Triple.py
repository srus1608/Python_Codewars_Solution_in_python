def pythagorean_triple(integers):
    # Sort the list to make it easy to find the largest integer
    a, b, c = sorted(integers)
    
    # Check if the sum of the squares of the two smaller numbers equals the square of the largest number
    return a**2 + b**2 == c**2