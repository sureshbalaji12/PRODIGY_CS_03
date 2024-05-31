import re

def check_password_strength(password):
    # Criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    digit_weight = 1
    special_char_weight = 2

    # Initialize scores
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    digit_score = 0
    special_char_score = 0

    # Calculate scores
    length_score = min(len(password), 10) * length_weight
    if re.search(r'[A-Z]', password):
        uppercase_score = uppercase_weight
    if re.search(r'[a-z]', password):
        lowercase_score = lowercase_weight
    if re.search(r'\d', password):
        digit_score = digit_weight
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        special_char_score = special_char_weight

    # Total score
    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    # Assess password strength
    if total_score < 8:
        return "Weak"
    elif total_score < 12:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
