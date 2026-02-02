age = int(input("Enter your age: "))
id_input = input("Do you have an ID card? (True/False): ").strip().lower()

# Graceful Boolean parsing
if id_input in ('true', 'yes', 'y', '1'):
    has_id = True
elif id_input in ('false', 'no', 'n', '0'):
    has_id = False
else:
    print("Invalid input for ID card. Please enter True or False.")
    has_id = False

if age >= 18 and has_id:
    print("Entry allowed")







