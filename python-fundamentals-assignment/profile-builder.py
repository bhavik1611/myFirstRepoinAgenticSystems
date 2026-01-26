user_name = input("Enter your name: ")
input_user_age = input("Enter your age: ")
user_age = int(input_user_age)  # Explicit type conversion to int

active_status_input = input("Are you an active user? (True / False): ")
# Clean up and convert input to boolean
is_active_user = active_status_input.strip().lower() == 'true'

print(f"User {user_name} is {user_age} years old. Active status: {is_active_user}")