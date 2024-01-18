import re

def is_valid_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    # Use the pattern to match the email address
    match = pattern.match(email)

    # If there is a match, it's a valid email address
    return bool(match)

# Example usage:
email_address = "rparmar229229@gmail.com"
if is_valid_email(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")
