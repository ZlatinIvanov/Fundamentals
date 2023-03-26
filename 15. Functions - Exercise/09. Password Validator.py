def is_valid_password(password):
    error_message = ""
    if len(password) < 6:
        error_message += "Password must be between 6 and 10 characters\n"
    elif len(password) > 10:
        error_message += "Password must be between 6 and 10 characters\n"
    if not all(c.isalnum() for c in password):
        error_message += "Password must consist only of letters and digits\n"

    if sum(c.isdigit() for c in password) < 2:
        error_message += "Password must have at least 2 digits"

    if error_message:
        print(error_message)
    else:
        print("Password is valid")


password = input()
is_valid_password(password)
