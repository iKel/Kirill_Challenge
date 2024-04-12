def is_valid_credit_card(number):
    # Check if the number starts with 4, 5, or 6
    if not number.startswith(('4', '5', '6')):
        return False
    
    # Remove hyphens if present
    number = number.replace('-', '')
    
    # Check if the number has exactly 16 digits
    if len(number) != 16 or not number.isdigit():
        return False
    
    # Check for 4 or more consecutive repeated digits
    for i in range(len(number) - 3):
        if number[i] == number[i + 1] == number[i + 2] == number[i + 3]:
            return False
    
    return True

# Test the function
card_numbers = [
    '4253625879615786',
    '4424424424442444',
    '5122-2368-7954-3214',
    '42536258796157867',  # Invalid: 17 digits
    '4424444424442444',   # Invalid: 4 consecutive repeated digits
    '5122-2368-7954 - 3214',  # Invalid: space as separator
]

for card in card_numbers:
    print(f'{card}: {is_valid_credit_card(card)}')
