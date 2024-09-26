def switch_gravity(lst):
    # Get the number of rows and columns
    rows = len(lst)
    cols = len(lst[0])
    
    # Create a new grid filled with empty spaces
    new_grid = [['-' for _ in range(cols)] for _ in range(rows)]
    
    for col in range(cols):
        # Count the number of `#` in the current column
        count_hashes = sum(1 for row in range(rows) if lst[row][col] == '#')
        
        # Place `#` at the bottom of the new column
        for row in range(rows - 1, rows - 1 - count_hashes, -1):
            new_grid[row][col] = '#'
    
    return new_grid