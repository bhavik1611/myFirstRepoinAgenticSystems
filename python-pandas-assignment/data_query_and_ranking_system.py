"""
AI Data Query and Ranking System
Simulate querying and analyzing an AI dataset using Pandas.
"""
import pandas as pd

def main():
    """
    Main function
    """
    # Step 1: Load the sample dataset
    csv_path = "./python-pandas-assignment/sample_dataset.csv"
    df = pd.read_csv(csv_path)

    # Step 2: Add Passed (Score >=40 is Passed) and Category columns if missing
    if 'Passed' not in df.columns:
        df['Passed'] = df['Score'] >= 40

    print("Original Dataset:")
    print(df, end="\n\n")

    # Step 3: Select a single column and print it
    print("Single column output -> Column: Name")
    print(df['Name'], end="\n\n")

    # Step 4: Select multiple columns and store in a new DataFrame
    cols = ['Name', 'Score', 'Category']
    print("Multiple columns output -> Columns: Name, Score, Category")
    print(df[cols], end="\n\n")

    # Step 5: Use iloc to retrieve the first three rows
    print("First three rows using iloc output:")
    print(df.iloc[:3], end="\n\n")

    # Step 6: Use loc after setting a meaningful index ('Name')
    df_indexed = df.set_index('Name')
    print("Loc output -> Index: Name, Value: Alice")
    print(df_indexed.loc['Alice'], end="\n\n")

    # Step 7: Filter rows where Score > 85
    print("Rows where Score > 85:")
    filtered_score = df[df['Score'] > 85]
    print(filtered_score, end="\n\n")

    # Step 8: Filter rows where Score > 85 and Passed is True
    print("Rows where Score > 85 and Passed is True:")
    filtered_score_passed = df[(df['Score'] > 85) & (df['Passed'])]
    print(filtered_score_passed, end="\n\n")

    # Step 9: Sort the filtered result in descending order of Score
    print("Rows where Score > 85 and Passed is True, sorted by Score (descending):")
    sorted_filtered = filtered_score_passed.sort_values(by='Score', ascending=False)
    print(sorted_filtered, end="\n\n")

    # Step 10: Chain filtering and sorting (Score > 80, Category == 'A', sorted by Score descending)
    print("High-performing Category A students (Score > 80, Category == 'A'), sorted by Score:")
    if 'Category' in df.columns:
        score_criteria = df['Score'] > 80
        category_criteria = df['Category'] == 'A'
        chain_filtered_sorted = df[score_criteria & category_criteria].sort_values(
            by='Score', ascending=False
        )
        print(chain_filtered_sorted[['Name', 'Score', 'Category']], end="\n\n")

if __name__ == "__main__":
    main()
