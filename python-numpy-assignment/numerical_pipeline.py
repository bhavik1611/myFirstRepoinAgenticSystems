"""
Python Numpy Assignment
NumPy: Numerical Foundations - Subjective - Rerelease
"""
import numpy as np

def main():
    """
    Main function
    """
    # 1. Creating a NumPy array representing numeric data (e.g., student scores)
    data = np.array([72, 45, 89, 55])

    # 2. Compute mean and standard deviation (vectorized)
    mean = np.mean(data)
    std = np.std(data)

    # 3. Normalize the data using vectorized arithmetic
    normalized = (data - mean) / std

    # 4. Reshape the normalized data into a 2D array with a valid shape
    two_d_reshaped = normalized.reshape(1, len(data))

    # 5. Print results in the requested format
    print(f"Original data: {data}")
    print(f"Mean: {mean:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print(f"Normalized data: {np.round(normalized, 2)}")
    print(f"Reshaped data:\n{np.round(two_d_reshaped, 2)}")
    print(f"Reshaped data shape: {two_d_reshaped.shape}")

if __name__ == "__main__":
    main()
