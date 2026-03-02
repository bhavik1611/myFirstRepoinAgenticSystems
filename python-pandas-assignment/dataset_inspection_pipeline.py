"""
AI Dataset Inspection Pipeline
Simulate the first stage of an AI data workflow using Pandas.
"""

import pandas as pd

def main():
    """
    Main function
    """
    # Step 1: Load the dataset using pd.read_csv()
    csv_path = "./python-pandas-assignment/sample_dataset.csv"
    print("Loading dataset from CSV...")
    df_loaded = pd.read_csv(csv_path)
    print("Dataset loaded.\n")

    # Step 2: Display the first 5 rows
    print("First 5 rows:")
    print(df_loaded.head(), end="\n\n")

    # Step 3: Display the last 5 rows
    print("Last 5 rows:")
    print(df_loaded.tail(), end="\n\n")

    # Step 4: Structural information (info)
    print("Dataset Info:")
    df_loaded.info()
    print()

    # Step 5: Summary statistics (describe)
    print("Summary Statistics:")
    print(df_loaded.describe(), end="\n\n")

    # Step 6: Select a single column ('Age'), store in variable
    print("Selecting a single column ('Age'):")
    age_series = df_loaded['Age']
    print(age_series, end="\n\n")

    # Step 7: Select multiple columns ('Name', 'Score'), store in new DataFrame
    print("Selecting multiple columns ('Name' and 'Score'):")
    name_score_df = df_loaded[['Name', 'Score']]
    print(name_score_df, end="\n\n")

    # Step 8: Filter rows based on a numerical condition (Score > 80)
    print("Filtered rows (Score > 80):")
    filtered_df = df_loaded[df_loaded['Score'] > 80]
    print(filtered_df, end="\n\n")

if __name__ == "__main__":
    main()
