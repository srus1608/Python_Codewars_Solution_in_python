def stringy(size):
    # Generate a base string with alternating '1's and '0's of length `size`
    base_string = '10' * (size // 2 + 1)  # Create a string longer than required
    return base_string[:size]  # Slice it to the exact length needed