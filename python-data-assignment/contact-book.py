# Simple Contact Book (Dictionary)

# Create the contact book dictionary with at least 3 contacts
contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Sunil": "9000012345"
}

# Print all contacts
print("Contact Book:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")

# Ask user for a name
search_name = input("Enter the name to look up: ")

# Display the phone number if found, else print not found message
if search_name in contacts:
    print(f"Phone number for {search_name}: {contacts[search_name]}")
else:
    print("Contact not found")
