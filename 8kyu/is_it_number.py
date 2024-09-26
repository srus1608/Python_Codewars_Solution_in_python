def is_digit(s):
    # Trim the input string to remove any leading or trailing whitespace
    s = s.strip()
    
    # Check if the string is empty after trimming
    if not s:
        return False
    
    try:
        # Try converting the string to a float
        float(s)
        return True
    except ValueError:
        # If conversion fails, it means the string is not a valid number
        return False