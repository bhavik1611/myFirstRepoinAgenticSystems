# Password Retry System

password = ""
required_password = "admin123"
while password != required_password:
    password = input("Enter your password: ")
    if password != required_password:
        print("Incorrect password. Please try again.")
print("Access granted")