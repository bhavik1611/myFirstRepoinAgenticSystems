def greeting(name):
    return f"Hello, {name}"

def calculate_scores(scores):
    num_subjects = len(scores)
    if num_subjects == 0:
        average = 0
    else:
        average = sum(scores) / num_subjects
    return num_subjects, average

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = input("Enter student's name: ")
    print(greeting(name))
    scores_input = input("Enter scores separated by spaces: ")
    # Convert the string input into a list of floats/ints
    scores = [float(s) for s in scores_input.strip().split()] if scores_input.strip() else []
    num_subjects, average = calculate_scores(scores)
    result = evaluate_result(average)

    print(f"Subjects: {num_subjects}")
    print(f"Average Score: {average:.1f}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()