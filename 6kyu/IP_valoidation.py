def is_valid_IP(strng):
    octets = strng.split('.')
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdigit():
            return False
        
        num = int(octet)
        
        if num < 0 or num > 255:
            return False
        
        if octet != str(num):  
            return False
            
    return True
 