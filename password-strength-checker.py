import re

def check_password_strength(password):
    # Define patterns for various criteria
    patterns = {
        'length': r'.{8,}',
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'digits': r'\d',
        'special_characters': r'[!@#$%^&*()\-_=+{};:,<.>]',
    }

    # Check each criteria
    strength = 0
    for pattern in patterns.values():
        if re.search(pattern, password):
            strength += 1

    # Return strength level
    return strength

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)

    if strength == 5:
        print("Strong password!")
    elif strength >= 3:
        print("Moderate password.")
    else:
        print("Weak password. Please choose a stronger one.")

if __name__ == "_main_":
    main()