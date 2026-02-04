# Employee Role Checker (Tuples + Sets)

# Store employee details as a tuple
employee = (101, "Alice", "IT")

# Store employee roles in a set
roles = {"admin", "editor", "viewer"}

# Print employee info using tuple indexing
print(f"Employee ID: {employee[0]}")
print(f"Name: {employee[1]}")
print(f"Department: {employee[2]}")

# Check for 'admin' role using set membership
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
