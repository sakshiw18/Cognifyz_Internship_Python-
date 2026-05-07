def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    strength = sum([has_upper, has_lower, has_digit, has_special, len(password) >= 8])

    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"

pwd = input("Enter password: ")
print(check_password_strength(pwd))