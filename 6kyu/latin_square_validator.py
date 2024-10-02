def validate_latin_square(square, m):
    n = len(square)
    
    # Check if the array is square
    if any(len(row) != n for row in square):
        return "Array not square"
    
    # Check if the array is of the correct size
    if n != m:
        return "Array is wrong size"
    
    # Check for values out of range and duplicates
    for i in range(n):
        row_seen = set()
        col_seen = set()
        
        for j in range(n):
            value = square[i][j]
            
            # Check for values out of range
            if value < 1 or value > m:
                return f"{value} at {i+1},{j+1} is not between 1 and {m}"
            
            # Check for duplicates in row
            if value in row_seen:
                return f"{value} occurs more than once in row {i+1}"
            row_seen.add(value)
            
            # Check for duplicates in column
            if square[j][i] in col_seen:
                return f"{square[j][i]} occurs more than once in column {i+1}"
            col_seen.add(square[j][i])
    
    # If all checks pass
    return f"Valid latin square of size {m}"