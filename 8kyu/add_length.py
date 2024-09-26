def add_length(str_):
    # Split the string into words
    words = str_.split()
    
    # Create a new list with each word followed by its length
    result = [f"{word} {len(word)}" for word in words]
    
    return result