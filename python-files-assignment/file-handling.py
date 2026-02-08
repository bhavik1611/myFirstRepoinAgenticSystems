import os

def read_numbers_from_file(file_path):
    """Reads integers from a text file, one per line, stripping whitespace."""
    numbers = []
    log_messages = []
    try:
        with open(file_path, 'r') as file:
            log_messages.append("[Info] File opened successfully")
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # Skip empty lines
                    try:
                        number = int(stripped_line)
                        numbers.append(number)
                    except ValueError:
                        log_messages.append(f"[Warning] Line '{stripped_line}' is not an integer")
    except FileNotFoundError:
        log_messages.append(f"[Error] File '{file_path}' not found")
        return [], log_messages
    except Exception as e:
        log_messages.append(f"[Error] Failed to open file: {e}")
        return [], log_messages
    return numbers, log_messages

def compute_statistics(numbers):
    """Returns the count, sum, and average of a list of numbers."""
    count = len(numbers)
    total = sum(numbers)
    average = total / count if count != 0 else 0
    return count, total, average

def log_results(log_file_path, messages):
    """Append log messages to the specified log file."""
    with open(log_file_path, 'a') as log_file:
        for message in messages:
            log_file.write(message + '\n')

def main():
    numbers_file = './python-files-assignment/numbers.txt'
    log_file = './python-files-assignment/results.log'
    log_entries = []

    # Read data
    numbers, read_log = read_numbers_from_file(numbers_file)
    log_entries.extend(read_log)

    # Data loaded step
    count = len(numbers)
    log_entries.append(f"[Info] Read {count} numbers: {numbers}")

    # Compute statistics
    count, total, average = compute_statistics(numbers)
    log_entries.append(f"[Info] Sum: {total}")
    log_entries.append(f"[Info] Average: {average}")
    log_entries.append("[Info] Processing completed")

    # Write log
    log_results(log_file, log_entries)

if __name__ == "__main__":
    main()