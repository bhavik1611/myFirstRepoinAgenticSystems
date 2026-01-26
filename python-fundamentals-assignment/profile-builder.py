# Validate name input (ensure it's non-empty and contains only letters and spaces)
while True:
    user_name = input("Enter your name: ").strip()
    if user_name and all(c.isalpha() or c.isspace() for c in user_name):
        break
    print("Invalid name. Please enter a valid name (letters and spaces only).")

# Validate age input (ensure it's a positive integer)
while True:
    input_user_age = input("Enter your age: ").strip()
    if input_user_age.isdigit() and int(input_user_age) > 0:
        user_age = int(input_user_age)
        break
    print("Invalid age. Please enter a positive integer.")

# Validate active status input (accept only 'True' or 'False', case insensitive)
while True:
    active_status_input = input("Are you an active user? (True / False): ").strip()
    if active_status_input.lower() in ('true', 'false'):
        is_active_user = active_status_input.strip().lower() == 'true'
        break
    print("Invalid input. Please enter 'True' or 'False'.")

print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")