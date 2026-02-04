
def odd_even_checker(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function from main code
if __name__ == "__main__":
    input_number = int(input("Enter a number: "))
    result = odd_even_checker(input_number)
    print(f"Number is {result}")