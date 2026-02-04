def add_two_numbers(a, b):
    return a + b

# Call the function from main code
if __name__ == "__main__":
    input_a = int(input("Enter the first number: "))
    input_b = int(input("Enter the second number: "))
    result = add_two_numbers(input_a, input_b)
    print(f"Sum is: {result}")