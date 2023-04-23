from string import ascii_letters, digits

line = input().split(", ")
allowed_chars = ascii_letters + digits + "_" + "-"

for username in line:
    if len(username) < 3 or len(username) > 16:
        continue
    not_valid = False
    for char in username:
        if char not in allowed_chars:
            not_valid = True
            break
    if not_valid:
        continue
    print(username)