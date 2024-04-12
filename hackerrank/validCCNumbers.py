import re

def is_valid_credit_card(number):
    # Regular expression for checking the format of the card number
    pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    
    # Check the basic pattern
    if not re.match(pattern, number):
        return "Invalid"
    
    # Remove hyphens to check for consecutive repeated digits
    number = number.replace("-", "")
    
    # Check for four or more consecutive repeated digits
    if re.search(r"(\d)\1{3,}", number):
        return "Invalid"
    
    return "Valid"

# Input handling
n = int(input().strip())
results = []
for _ in range(n):
    credit_card_number = input().strip()
    result = is_valid_credit_card(credit_card_number)
    results.append(result)

# Output results
for result in results:
    print(result)


# Tests
# 6               
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456