def who_is_paying(name):
    if len(name) <= 2:
        # If the name is 2 characters or less, return the name as is
        return [name]
    else:
        # Otherwise, return the full name and the first two letters of the name
        return [name, name[:2]]