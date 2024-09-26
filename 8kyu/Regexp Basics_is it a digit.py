def is_digit(n):
    # Check if n is a string and has exactly one character
    if isinstance(n, str) and len(n) == 1:
        # Check if the single character is a digit
        return n.isdigit()
    return False