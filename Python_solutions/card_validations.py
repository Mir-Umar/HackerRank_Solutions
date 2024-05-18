import re
def is_valid(card_number):
    # Basic pattern check for the format and starting digit
    pattern = r"^(?:4|5|6)(?:\d{15}|\d{3}(?:-\d{4}){3})$"
    if not re.match(pattern, card_number):
        return False

    card_number = card_number.replace("-", "")
    
    # Check for four or more consecutive repeated digits
    if re.search(r"(\d)\1{3}", card_number):
        return False
    
    return True
    

if __name__ == "__main__":
    num_cases = int(input())
    for i in range(num_cases):
        if is_valid(input()):
            print("Valid")
        else:
            print("Invalid")
