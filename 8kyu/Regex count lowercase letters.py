def lowercase_count(strng):
    # Count lowercase letters using a list comprehension and str.islower() method
    return sum(1 for char in strng if char.islower())