# Student Marks Analyzer (Lists + Slicing)

def analyze(marks):
    # Print the full list of marks
    print(f"All marks: {marks}")

    # Print the first 3 marks using slicing
    print(f"First 3 marks: {marks[:3]}")

    # Print the last 3 marks using slicing
    print(f"Last 3 marks: {marks[-3:]}")

    # Calculate and print the highest, lowest, and average mark
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Average: {average:.2f}")

# Take marks of at least 8 students as input
marks_input = input("Enter marks of at least 8 students, separated by spaces: ")
marks_list = [int(x) for x in marks_input.strip().split()]

# Simple validation to check if at least 8 marks are entered
if len(marks_list) < 8:
    print("Please enter at least 8 marks.")
else:
    analyze(marks_list)
