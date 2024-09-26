import urllib.parse

def generate_link(user):
    # Use urllib.parse.quote to encode the user string properly
    encoded_user = urllib.parse.quote(user)
    
    # Construct and return the full URL
    return f'http://www.codewars.com/users/{encoded_user}'