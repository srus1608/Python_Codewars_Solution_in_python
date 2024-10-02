
def count(s):
    if not s:
        return {}
    character_count={}
    for char in s:
        if char in character_count:
            character_count[char]+=1
        else:    
            character_count[char] = 1

    # The function code should be here
    return character_count