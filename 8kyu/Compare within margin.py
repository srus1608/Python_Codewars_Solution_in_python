def close_compare(a, b, margin=0):
    # Calculate the absolute difference between a and b
    difference = abs(a - b)
    
    # Compare the difference with the margin
    if difference <= margin:
        return 0
    elif a < b:
        return -1
    else:
        return 1