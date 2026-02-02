account_balance = int(input("Enter your account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))
verification_input = input("Are you a verified user? (True/False): ").strip().lower()

if verification_input in ('true', 'yes', 'y', '1'):
    is_verified = True
elif verification_input in ('false', 'no', 'n', '0'):
    is_verified = False
else:
    print("Invalid input for verification status. Please enter True or False.")
    is_verified = False

if is_verified and withdrawal_amount <= account_balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")