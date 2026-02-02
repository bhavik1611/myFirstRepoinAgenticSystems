accuracy = input("Enter the accuracy of the model: ")
# validate if the input is numeric
try:
    accuracy_val = float(accuracy)
    print(f"Model accuracy is {accuracy_val:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()