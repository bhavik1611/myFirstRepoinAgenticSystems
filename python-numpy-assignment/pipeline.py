"""
Python Numpy Assignment
"""

import numpy as np

np.random.seed(42)

def generate_random_data(rows, columns):
    """
    Generate random data for the rows (represents samples) and columns (represents features)
    rows: number of samples
    columns: number of features
    """
    return np.random.rand(rows, columns)

def calculate_statistics(data, axis=None):
    """
    Calculate the statistics of the data
    data: numpy array
    axis: axis along which the statistics are calculated
    """
    mean = np.mean(data, axis=axis)
    std = np.std(data, axis=axis)
    return mean, std

def normalize_data(data, mean, std):
    """
    Normalize the data
    data: numpy array
    mean: mean of the data
    std: standard deviation of the data
    """
    normalized_data = (data - mean) / std
    return normalized_data

def split_data(data, split_ratio):
    """
    Split the data into training and testing sets
    data: numpy array
    split_ratio: ratio of training data to testing data
    """
    train_size = int(len(data) * split_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

def main():
    """
    Main function
    """
    # Taking the input from the user
    rows = int(input("Enter the number of samples required in the dataset: "))
    columns = int(input("Enter the number of features required in the dataset: "))

    # Generating the random data
    data = generate_random_data(rows, columns)
    print(f"Original Data Shape: {data.shape}")
    print(f"Original Data: {data}")

    # Calculating the statistics of the data
    mean, std = calculate_statistics(data, axis=0)
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std}")

    # Normalizing the data
    normalized_data = normalize_data(data, mean, std)
    print(f"Normalized Data: {normalized_data}")

    # Splitting the data into training and testing sets
    train_data, test_data = split_data(normalized_data, 0.8)
    print(f"Train Data Shape: {train_data.shape}")
    print(f"Test Data Shape: {test_data.shape}")

    train_data[0][0] = 100

    if normalized_data[0][0] == 100:
        print("The value of original data is changed")
    else:
        print("The value of original data is not changed")

    print(f"Train Data: {train_data}")
    print(f"Original Data: {normalized_data}")


if __name__ == "__main__":
    main()
